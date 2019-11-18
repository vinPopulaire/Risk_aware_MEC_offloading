'''
Parameters of the simulation
'''

import numpy as np
import dill

SAVE_FIGS = False
ONE_FIGURE = False
GENERATE_FIGURES = False
LOAD_SAVED_PARAMETERS = False
SAVE_PARAMETERS = False
SAVE_RESULTS = True

def set_parameters(case):
CONSTANT_OFFLOADING = False

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
        Amount of data a user has
    dn: 1-D array
        Cycles each user's job needs
    fn: 1-D array
        Computational capability of the user
    gn: 1-D array
        Coefficient denoting the consumed energy per cycle locally
    tn: 1-D array
        Time to process the data locally by each user
    en: 1-D array
        Energy to process the data locally by each user
    e1: float
        Error for user offloading convergence
    an: float
        Parameter of prospect theory utility
    kn: float
        Weighting factor that captures sensitivity of players toward losses as compared to gains
    c: 1-D array
        Each column repesents the pricing factor for each user
    '''

    N = 25
    e1 = 1

    an = 0.2
    kn = 0.31

    if case["users"] == "homo":
        bn = 10*1e6 * np.ones(N)
        dn = 8*1e9 * np.ones(N)

        fn = 6e9 * np.ones(N)
        gn = 4e-9 * np.ones(N)

    if case["users"] == "hetero":
        bn = 1e6 * (np.random.uniform(0, 9, size=N) + 1)
        dn = 8*1e9 * np.ones(N)

        fn = 6e9 * np.ones(N)
        gn = 4e-9 * np.ones(N)

    tn = dn/fn
    en = gn*dn

    # we want that c is less than the equation so we set it equal to to equation * 1/2
    c = 0.2 * bn/dn * (1 - (1/(tn*en)))

    assert c.all() > 0, "c should be positive"

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
