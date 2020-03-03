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

    # to generate the first expected utility
    expected_utility = np.empty_like(b)
    for i in range(len(b)):
        expected_utility[i] = -utility_function(0, i, b, **params)
    expected_utility_converging = [expected_utility]
    pricing_converging = [calculate_costs(b, **params)]
    PoF_converging = [calculate_PoF(b, **params)]

    while not converged:

        # if constant offloading, just calculate the expected utility for the specified offloading amount
        if params["CONSTANT_OFFLOADING"]:
            expected_utility = np.empty_like(b)
            for i in range(len(b)):
                expected_utility[i] = -utility_function(b[i], i, b, **params)
            b_old = b.copy() # to converge
        else:
            b, expected_utility = play_offloading_game(b, **params)

        # check if the game has reached a Nash equilibrium
        converged = game_converged(b, b_old, **params)

        b_old = b.copy()

        iterations += 1
        b_converging.append(b.copy())
        expected_utility_converging.append(expected_utility.copy())
        pricing_converging.append(calculate_costs(b, **params))
        PoF_converging.append(calculate_PoF(b, **params))

    user_energy = calculate_user_energy(b, PoF_converging[-1], **params)

    if params["GENERATE_CONVERGING_FIGURES"]: plot_b_converging(b_converging, params)
    if params["GENERATE_CONVERGING_FIGURES"]: plot_expected_utility_converging(expected_utility_converging, params)
    if params["GENERATE_CONVERGING_FIGURES"]: plot_pricing_converging(pricing_converging, params)
    if params["GENERATE_CONVERGING_FIGURES"]: plot_PoF_converging(PoF_converging, params)
    if params["GENERATE_CONVERGING_FIGURES"]: plot_expected_utility_and_pricing_converging(expected_utility_converging, pricing_converging, params)

    results = {
        "params": params,
        "b": b,
        "expected_utility": expected_utility,
        "iterations": iterations + 1, # add 1 to show the number of iterations
        "pricing": calculate_costs(b, **params) ,
        "PoF": calculate_PoF(b, **params),
        "b_converging": b_converging,
        "expected_utility_converging": expected_utility_converging,
        "pricing_converging": pricing_converging,
        "PoF_converging": PoF_converging,
        "user_energy": user_energy,
            }

    return results
