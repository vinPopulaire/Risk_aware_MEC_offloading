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

from parameters import *
from helper_functions import *
from pricing_aware_MEC_offloading import *

import time
import dill

# Keep only three decimal places when printing numbers
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

case = {"users": "homo"}

for repetition in range(1):
    print("Repetition no: " + str(repetition+1))

    results = {}

    if LOAD_SAVED_PARAMETERS == True:
        params = load_parameters()
    else:
        # Set random parameter in order to generate the same parameters
        print("Generating new parameters")
        np.random.seed(13)
        params = set_parameters(case)

    N = params['N']

    start = time.time()

    # Run main simulation
    results = main(params)
    # check_all_parameters(**params)
    # check_best_parameters(**params)

    end = time.time()
    running_time = end - start
    print("Time of simulation:")
    print(running_time)

    if SAVE_PARAMETERS == True:
        save_parameters(params)

