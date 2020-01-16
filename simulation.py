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
# Ns = [1,2,5,10,25,50,75,100]
Ns = [25]
cpars = np.linspace(0.1,0.9,33)
# cpars = [0.5]

for N in Ns:
    for cpar in cpars:
        for repetition in range(1):
            print("Repetition no: " + str(repetition+1))

            results = {}

            if LOAD_SAVED_PARAMETERS == True:
                params = load_parameters(cpar)
            else:
                # Set random parameter in order to generate the same parameters
                print("Generating new parameters")
                np.random.seed()
                params = set_parameters(case, N, cpar)

            N = params['N']
            print("Number of users: " + str(N))

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

            results["time"] = running_time
            results["repetition"] = repetition

            if SAVE_RESULTS == True:
                if CONSTANT_OFFLOADING:
                    constant_str = "_b_constant_" + str(int(results["b"][0]/1e6)) + "_"
                else:
                    constant_str = ""
                outfile = 'saved_runs/results/individual/' + case["users"] + constant_str + "_N_" + str(N) + "_c_" + str(round(cpar,3)) + "_" + str(repetition)

                with open(outfile, 'wb') as fp:
                    dill.dump(results, fp)

if GENERATE_FIGURES and not SAVE_FIGS:
    plt.show()
