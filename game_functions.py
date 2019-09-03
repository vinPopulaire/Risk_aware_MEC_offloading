'''
Game theory functions
'''

import numpy as np
from scipy.optimize import fmin
import math


def play_offloading_game(b, costs, bn, dn, an, kn, c, tn, en, **params):

    # sum of all responses
    B = np.sum(b)
    Bn = np.sum(bn)
    Dn = np.sum(dn)

    # Best response of all users except the user
    B_minus_u = B - b
    Bn_minus_u = Bn - bn
    Dn_minus_u = Dn - dn

    b_new = np.empty_like(b)

    for i in range(len(b)):
        # find best response of each one based on utility
        b_new[i] = fmin(utility_function, 0, args=(Dn_minus_u[i], B_minus_u[i], Bn_minus_u[i], dn[i], bn[i], an, kn, c[i], tn[i], en[i]), disp=False)

    # print(b)
    # print(b_new)

    return b_new

def game_converged(b, b_old, e1, **params):
    '''
    Check if the game has converged

    Parameters
    ----------

    b: 1-D array
        The offloading values the users chose on the last game
    b_old: 1-D array
        The offloading values the users chose on the previous game
    e1: float
        Error for user offloading convergence

    Returns
    -------

    convergence: Boolean
        Boolean on whether all users are sure of the selected server or not
    '''

    # e1 is the error tolerance defined in parameters
    if (np.abs(b - b_old) < e1).all():
        return True
    return False

def utility_function(b, Dn_minus_u, B_minus_u, Bn_minus_u, dn, bn, an, kn, c, tn, en):
    # ATTENTION here all variables are single values and not np.arrays

    dt = ((Dn_minus_u + dn) * (B_minus_u + b) / (Bn_minus_u + bn)) / (Dn_minus_u + dn)

    Pr = dt**2

    ROR = (2-math.exp(dt-1) - 1/(tn*en) - c*dn/bn)**an

    expected_utility = b**an * (ROR * (1 - Pr) - kn * (1/(tn*en) + c*dn/bn)**an * Pr)

    # return minus the utility because we will to use a minimization optimization even
    # though we want to maximize the utility
    return -expected_utility
