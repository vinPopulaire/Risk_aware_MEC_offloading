'''
Helper functions that are used in the simulation
'''

import numpy as np

from game_functions import *

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
    b_old: 1-D array
        Each column represents the amount of data a user wanted to offload on the previous round
        to the MEC server.
    '''

    b = 0*1e6 * np.ones(N)

    # set b_old different to b so that we don't falsely converge
    b_old = 1 * np.ones(N)

    return b, b_old

def calculate_costs(b, bn, dn, c, **params):
    '''
    Calcuate costs imposed by the MEC server to each user

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

def check_all_parameters(bn, dn, an, kn, c, tn, en, **params):

    working = 0
    eps = 10
    for an1 in np.linspace(0.3, 1, 8):
        an = an1

        for kn1 in np.linspace(0.1, 2, 10):
            kn = kn1
            working += 1
            print(working)

            for dn1 in np.linspace(1, 10, 10):
                dn = dn1 * 1e9 * np.ones(params["N"])

                for fn1 in np.linspace(1, 10, 10):
                    fn = fn1 * 1e9 * np.ones(params["N"])
                    tn = dn/fn

                    for gn1 in np.linspace(1, 10, 10):
                        gn = gn1 * 1e-9 * np.ones(params["N"])
                        en = gn * dn

                        for bn1 in np.linspace(1, 10, 10):
                            bn = bn1 * 1e6 * np.ones(params["N"])

                            for c1 in np.linspace(2e-1, 9e-1, 8):
                                c = c1 * bn/dn * (1 - (1/(tn*en)))

                                if c.all() > 0:

                                    counter = 0

                                    for i, value in enumerate(np.linspace(0,bn[0],11)):

                                        b_others = value * np.ones(5)

                                        res = fminbound(utility_function, 0, bn[0], args=(0, b_others, dn, bn, an, kn, c, tn, en), disp=False)
                                        result_utility = -utility_function(res, 0, b_others, dn, bn, an, kn, c, tn, en)

                                        if (res > eps) and (res <  bn[0] - eps) and (np.isfinite(result_utility)):
                                            counter += 1

                                    if counter > 8:
                                        my_string = ("Counter: " + str(counter) + "\n" +
                                            "an: " + str(an) +
                                            " kn: " + str(kn) +
                                            " bn: " + str(bn1) +
                                            " dn: " + str(dn1) +
                                            " fn: " + str(fn1) +
                                            " gn: " + str(gn1) +
                                            " c: " + str(c1) + "\n")

                                        with open('result.txt' , 'a') as writer:
                                            writer.write(my_string)

    return "Done"

def check_best_parameters(bn, dn, an, kn, c, tn, en, **params):

    N = 10000

    fig, ax = plt.subplots(11,1)

    for i, value in enumerate(np.linspace(0,bn[0],11)):

        b_others = value * np.ones(5)

        eps = 0.2
        res = fminbound(utility_function, 0, bn[0], args=(0, b_others, dn, bn, an, kn, c, tn, en), disp=False)
        result_utility = -utility_function(res, 0, b_others, dn, bn, an, kn, c, tn, en)

        if (res > eps) and (res <  bn[0] - eps) and (np.isfinite(result_utility)):
            print()
            print(res)
            print(result_utility)

        x = np.linspace(0, bn[0], N)
        res = np.empty_like(x)
        for j in range(len(x)):
            res[j] = -utility_function(x[j], 0, b_others, dn, bn, an, kn, c, tn, en)


        plt.subplot(11,1,i+1)
        plt.suptitle("an: " + str(an) +
                " bn: " + str(bn[0]) +
                " dn: " + str(dn[0]) +
                " kn: " + str(kn) +
                " tn: " + str(tn[0]) +
                " en: " + str(en[0]) +
                " c: " + str(c[0]), fontsize=6)
        plt.plot(x, res)

    plt.show()

    return "Done"
