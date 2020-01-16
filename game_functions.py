'''
Game theory functions
'''

import numpy as np
from scipy.optimize import fminbound
import math
import matplotlib.pyplot as plt
import pdb
import time


def play_offloading_game(b, bn, dn, an, kn, c, tn, en, **params):

    b_new = np.empty_like(b)
    expected_utility = np.empty_like(b)

    # N = 10000
    # plt.figure(figsize=(40.0, 30.0))

    for i in range(len(b)):
        # find best response of each one based on utility
        b_new[i], expected_utility[i], _, _ = fminbound(utility_function, 0, bn[i], args=(i, b, dn, bn, an, kn, c, tn, en), disp=False, full_output=True)

        b[i] = b_new[i]

        # calculate utility for ploting
        # x = np.linspace(0, bn[i], N)
        # res = np.empty_like(x)

        # for j in range(len(x)):
        #     res[j] = -utility_function(x[j], i, b, dn, bn, an, kn, c, tn, en)

        # plt.subplot(5,1,i+1)
        # plt.plot(x, res)

    # plt.show(block=False)

    return b_new, -expected_utility

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

def utility_function(x, i, b, dn, bn, an, kn, c, tn, en, **params):
    # ATTENTION here all variables are np.arrays
    # EXCEPT from x and i which are single values

    # replace user's i offloading value
    b_replaced = np.copy(b)
    b_replaced[i] = x

    # dt = 1/(1+np.exp(-1.2e-11*np.sum(dn*b_replaced/bn)))
    dt = -1 + 2/(1+np.exp(-2.0e-11*np.sum(dn*b_replaced/bn)))

    Pr = dt**2

    ROR = (2-math.exp(dt-1) - 1/(tn[i]*en[i]) - c[i]*dn[i]/bn[i])**an

    expected_utility = x**an * (ROR * (1 - Pr) - kn * (1/(tn[i]*en[i]) + c[i]*dn[i]/bn[i])**an * Pr)

    # return minus the utility because we will to use a minimization optimization even
    # though we want to maximize the utility
    return -expected_utility
