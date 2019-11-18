# -*- coding: utf-8 -*-
"""
    Pricing_aware_MEC_offloading.simulation
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Simulation for the Pricing_aware_MEC_offloading

    :copyright: (c) 2019 by Giorgos Mitsis.
    :license: MIT License, see LICENSE for more details.
"""

import numpy as np
import matplotlib.pyplot as plt

from helper_functions import *
from game_functions import *
from plots import *

from parameters import *

def main(params):

    # b_old is only used to store the previous offloading decision to find convergence
    b,b_old = initialize(**params)

    converged = False

    iterations = 0
    b_converging = [b.copy()]
    while not converged:

        # if constant offloading, just calculate the expected utility for the specified offloading amount
        if CONSTANT_OFFLOADING:
            expected_utility = np.empty_like(b)
            for i in range(len(b)):
                expected_utility[i] = -utility_function(b[i], i, b, params["dn"], params["bn"],params["an"], params["kn"], params["c"], params["tn"], params["en"])
            b_old = b.copy() # to converge
        else:
            b, expected_utility = play_offloading_game(b, **params)

        # check if the game has reached a Nash equilibrium
        converged = game_converged(b, b_old, **params)

        b_old = b.copy()

        iterations += 1
        b_converging.append(b.copy())

    if GENERATE_FIGURES: plot_b_converging(b_converging)

    results = {
        "b": b,
        "expected_utility": expected_utility,
        "iterations": iterations + 1, # add 1 to show the number of iterations
            }

    return results
