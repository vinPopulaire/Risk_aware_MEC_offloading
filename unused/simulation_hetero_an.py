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
N = 25

an = 0.2 * np.ones(N)

kn = 1.2 * np.ones(N)

# Set random parameter in order to generate the same parameters
print("Generating new parameters")
np.random.seed()
params = set_parameters(case, N)

# repeat if any of the values is negative since we want an to be positive and less than 1
an = np.random.uniform(0.2,0.5, size=N)
while np.any(an <= 0) and np.any(an >= 1):
    print(an)
    an = np.random.uniform(0.2,0.5, size=N)
print(an)

params["an"] = an

for repetition in range(1):
    print("Repetition no: " + str(repetition+1))

    results = {}

    start = time.time()

    # Run main simulation
    results = main(params)
    # check_all_parameters(**params)
    # check_best_parameters(**params)

    end = time.time()
    running_time = end - start
    print("Time of simulation:")
    print(running_time)

    results["N"] = N
    results["time"] = running_time
    results["repetition"] = repetition

    if params["SAVE_RESULTS"] == True:
        outfile = 'saved_runs/results/individual/' + "hetero_an_" + str(np.round(np.mean(an), 3)) + '_' + str(repetition)

        with open(outfile, 'wb') as fp:
            dill.dump(results, fp)

an = np.mean(an) * np.ones(N)
params["an"] = an

print("Mean an: " + str(np.round(an, 3)))

for repetition in range(1):
    print("Repetition no: " + str(repetition+1))

    results = {}

    start = time.time()

    # Run main simulation
    results = main(params)
    # check_all_parameters(**params)
    # check_best_parameters(**params)

    end = time.time()
    running_time = end - start
    print("Time of simulation:")
    print(running_time)


    results["N"] = N
    results["time"] = running_time
    results["repetition"] = repetition

    if params["SAVE_RESULTS"] == True:
        outfile = 'saved_runs/results/individual/' + "homo_an_" + str(np.round(np.mean(an), 3)) + '_' + str(repetition)

        with open(outfile, 'wb') as fp:
            dill.dump(results, fp)



# PLOTS different an

repetition = 0

homo = []
hetero = []

mean_expected_utility = []
mean_b = []
mean_pricing = []
PoF = []

mean_energy = []

infile = 'saved_runs/results/individual/' + "homo_an_" + str(np.round(np.mean(an), 3)) + '_' + str(repetition)
with open(infile, 'rb') as in_strm:
    kati = dill.load(in_strm)
    expected_utility_homo = kati["expected_utility"].copy()
    b_homo = kati["b"].copy()
    pricing_homo = kati["pricing"].copy()
    PoF_homo = kati["PoF"].copy()

    user_energies_homo = kati["user_energy"].copy()

    params_homo = kati["params"]

homo = (np.mean(expected_utility_homo), np.mean(b_homo), np.mean(pricing_homo), PoF_homo, np.mean(user_energies_homo))

infile = 'saved_runs/results/individual/' + "hetero_an_" + str(np.round(np.mean(an), 3)) + '_' + str(repetition)
with open(infile, 'rb') as in_strm:
    kati = dill.load(in_strm)
    expected_utility_hetero = kati["expected_utility"].copy()
    b_hetero = kati["b"].copy()
    pricing_hetero = kati["pricing"].copy()
    PoF_hetero = kati["PoF"].copy()

    user_energies_hetero = kati["user_energy"].copy()

    params_hetero = kati["params"]

hetero = (np.mean(expected_utility_hetero), np.mean(b_hetero), np.mean(pricing_hetero), PoF_hetero, np.mean(user_energies_hetero))

n_groups = 5
labels = ["Homo", "Hetero"]
x = np.arange(len(labels))

fig, axs = plt.subplots(2,2)
fig.suptitle('Heterogeneous an')

bar_width = 0.45
opacity = 0.8

axs[0,0].bar(0.1, homo[0], bar_width, alpha=opacity, color='0.7', label="Homo")
axs[0,0].bar(bar_width + 0.15, hetero[0], bar_width, alpha=opacity, color='0.5', label="Hetero")
axs[0,0].set_title('Expected Utility')


axs[0,1].bar(0.1, homo[1], bar_width, alpha=opacity, color='0.7', label="Homo")
axs[0,1].bar(bar_width + 0.15, hetero[1], bar_width, alpha=opacity, color='0.5', label="Hetero")
axs[0,1].set_title('Offloading Data')
axs[0,1].ticklabel_format(style='sci', axis='y', scilimits=(6,6))

axs[1,0].bar(0.1, homo[2], bar_width, alpha=opacity, color='0.7', label="Homo")
axs[1,0].bar(bar_width + 0.15, hetero[2], bar_width, alpha=opacity, color='0.5', label="Hetero")
axs[1,0].set_title('Pricing')
axs[1,0].ticklabel_format(style='sci', axis='y', scilimits=(6,6))

axs[1,1].bar(0.1, homo[3], bar_width, alpha=opacity, color='0.7', label="Homo")
axs[1,1].bar(bar_width + 0.15, hetero[3], bar_width, alpha=opacity, color='0.5', label="Hetero")
axs[1,1].set_title('PoF')

plt.subplots_adjust(hspace = 0.3)
plt.setp(axs, xticks=[0.1, bar_width+0.15], xticklabels=labels)

path_name = "hetero_an_" + str(np.round(np.mean(an),3)) + "_utility_bars"
plt.savefig("plots/" + path_name + ".png")
