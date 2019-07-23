'''
Parameters of the simulation
'''

import numpy as np
import dill

SAVE_FIGS = False
ONE_FIGURE = False
LOAD_SAVED_PARAMETERS = False
SAVE_PARAMETERS = False
SAVE_RESULTS = False

def set_parameters(case):
    '''
    Sets the parameters used in the simulation

    Parameters
    ----------

    case: dictionary
        Dictionary containing infromation about whether the user homogeneous or heterogeneous

    Returns
    ----------

    N: int
        Number of users
    bn: 1-D array
        Each column represents the amount of data a user has.
    dn: 1-D array
        Each column represents the cycles each user's job needs.
    fn: 1-D array
        Each column represents the computational capability of the user
    gn: 1-D array
        Each column represents the coefficient denoting the consumed energy per cycle locally
    e1: float
        Error for user offloading convergence
    an: float
        Parameter of prospect theory utility
    c: 1-D array
        Each column repesents the pricing factor for each user
    '''

    N = 5
    e1 = 1e-03

    an = 0.5

    if case["users"] == "homo":
        bn = 5*1e6 * np.ones(N)
        dn = 2*1e9 * np.ones(N)

        fn = 1e9 * np.ones(N)
        gn = 1e-9 * np.ones(N)

    tn = dn/fn
    en = gn*dn

    # we want that c is less than the equation so we set it equal to to equation * 1/2
    c = 1/2 * bn/dn * (1 - (1/(tn*en)))

    return locals()

def load_parameters():
    '''
    Loads the parameters from a file

    Returns
    ----------

    params: dictionary
        Dictionary with the paramters of the simulation
    '''
    print("Loading parameters")
    infile = "runs/parameters/" + "parameters"

    with open(infile, 'rb') as in_strm:
        params = dill.load(in_strm)

    return params

def save_parameters(params):
    '''
    Saves the parameters in a file

    Parameters
    ----------

    params: dictionary
        Dictionary with the paramters of the simulation
    '''
    outfile = "runs/parameters/" + "parameters"

    with open(outfile, 'wb') as fp:
        dill.dump(params, fp)
