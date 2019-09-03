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

def main(params):

    # b_old is only used to store the previous offloading decision to find convergence
    b,b_old = initialize(**params)

    converged = False
    while not converged:

        # find cost set by the MEC server to each user
        costs = set_costs(b, **params)

        b = play_offloading_game(b, costs, **params)

        # check if the game has reached a Nash equilibrium
        converged = game_converged(b, b_old, **params)

        b_old = b

    results = {
        "b": b,
            }

    return results
