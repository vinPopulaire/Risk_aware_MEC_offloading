'''
Game theory functions
'''

import numpy as np


def game_converged(b, b_old, e1, **params):
    '''
    Check if the game has converged

    Parameters
    ----------

    b: 1-D array
        The offloading values the users chose on the last game
    b_old: 1-D array
        The offloading values the users chose on the previous game

    Returns
    -------

    convergence: Boolean
        Boolean on whether all users are sure of the selected server or not
    '''

    # e1 is the error tolerance defined in parameters
    if (np.abs(b - b_old) < e1).all():
        return True
    return False

