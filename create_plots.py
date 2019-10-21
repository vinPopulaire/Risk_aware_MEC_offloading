'''
Plot functions
'''

import numpy as np
from game_functions import *


def plot_utility_functions(b, bn, dn, an, kn, c, tn, en, **params):
    N = 10000

    for i in range(len(b)):
        x = np.linspace(0, bn[i], N)
        res = np.empty_like(x)

        for j in range(len(x)):
            res[j] = -utility_function(x[j], i, b, dn, bn, an, kn, c, tn, en)

        plt.subplot(5,1,i+1)
        plt.plot(x, res)
    plt.show()

