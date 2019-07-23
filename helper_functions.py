'''
Helper functions that are used in the simulation
'''

import numpy as np

def initialize(N, **params):
    '''
    Initialize the probabilities for the simulation

    Parameters
    ----------

    N: int
        Number of users

    Returns
    -------

    b: 1-D array
        Each column represents the amount of data a user wants to offload to the MEC server.
    '''

    b = 0.5 * np.ones(N)

    # set b_old different to b so that we don't falsely converge
    b_old = 1 * np.ones(N)

    return b, b_old

def set_costs(b, bn, dn, c, **params):
    '''
    Set costs imposed by the MEC server to each user

    Parameters
    ----------

    b: 1-D array
        Each column represents the amount of data a user wants to offload to the MEC server.
    bn: 1-D array
        Each column represents the amount of data a user has.
    dn: 1-D array
        Each column represents the cycles each user's job needs.
    c: 1-D array
        Each column repesents the pricing factor for each user

    Returns
    -------

    costs: 1-D array
        Each column contains the cost imposed by the MEC server to each user
    '''

    costs = c * dn * b/bn

    return costs
