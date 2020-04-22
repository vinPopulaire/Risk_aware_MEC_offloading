'''
Parameters of the simulation
'''

import numpy as np
import dill

def set_parameters(case, N):
    '''
    Sets the parameters used in the simulation

    Parameters
    ----------

    case: dictionary
        Dictionary containing infromation about whether the user homogeneous or heterogeneous
    N: int
        Number of users

    Returns
    ----------

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
    an: 1-D array
        Parameter of prospect theory utility
    kn: 1-D array
        Weighting factor that captures sensitivity of players toward losses as compared to gains
    cpar: float
        The parameter used to set the cost for users
    bpar: float
        The parameter used to set the initial offloading of users
    c: 1-D array
        Each column repesents the pricing factor for each user
    fixed_transm_rate : float
        The transmission rate for offloading 1 bit per second [fixed]
    fixed_transm_power : float
        The transmission power used for the transmission [fixed]
    '''

    SAVE_FIGS = True
    ONE_FIGURE = False
    GENERATE_FIGURES = True
    GENERATE_CONVERGING_FIGURES = True
    LOAD_SAVED_PARAMETERS = False
    SAVE_PARAMETERS = False
    SAVE_RESULTS = True

    CONSTANT_OFFLOADING = False

    e1 = 10000

    if case["users"] == "homo":
        bn = 10*1e6 * np.ones(N) + np.random.uniform(-1, 1, size=N) * 1e6
        dn = 8*1e9 * np.ones(N) + np.random.uniform(-1,1, size=N) * 1e9

        fn = 6e9 * np.ones(N) + np.random.uniform(-1,1, size=N) * 1e9
        gn = 4e-9 * np.ones(N) + np.random.uniform(-1,1, size=N) * 1e-9

        an = 0.2 * np.ones(N)
        kn = 1.2 * np.ones(N)

    if case["users"] == "hetero":
        bn = 10*1e6 * np.ones(N)
        dn = 8*1e9 * np.ones(N)

        fn = 6e9 * np.ones(N)
        gn = 4e-9 * np.ones(N)

        # TODO change to heterogeneous users
        an = 0.2 * np.ones(N)
        kn = 1.2 * np.ones(N)

    tn = dn/fn
    en = gn*dn

    # we want that c is less than the equation so we set it equal to to equation * 1/2
    cpar = 0.5
    c = cpar * bn/dn * (1 - (1/(tn*en)))

    assert c.all() > 0, "c should be positive"

    bpar = 0

    fixed_transm_rate = 1*1e9
    fixed_transm_power = 0.1

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
    infile = "saved_runs/parameters/" + "parameters"

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
    outfile = "saved_runs/parameters/" + "parameters"

    with open(outfile, 'wb') as fp:
        dill.dump(params, fp)
