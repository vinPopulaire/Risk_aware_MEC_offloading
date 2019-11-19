'''
Plot functions to graphically present simulation results
'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from parameters import SAVE_FIGS, ONE_FIGURE

def setup_plots(suptitle):

    '''
    Basic setup of plots so it can be reused on plot functions

    Parameters
    ----------

    suptitle: string
        Description of the plot that will appear on the top

    Returns
    -------

    Figure and axis matplotlib structs

    '''
    fig, ax = plt.subplots(1, 1, figsize=(15, 12))
    fig.suptitle(suptitle)
    # for item in ([ax.title, ax.xaxis.label, ax.yaxis.label]):
    #     item.set_fontsize(30)
    # for item in (ax.get_xticklabels() + ax.get_yticklabels()):
    #     item.set_fontsize(26)
    #     item.set_fontweight("bold")
    # font = {'weight' : 'bold'}
    # matplotlib.rc('font', **font)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Provide tick lines across the plot to help viewers trace along
    # the axis ticks.
    plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)

    # Remove the tick marks; they are unnecessary with the tick lines we just
    # plotted.
    plt.tick_params(axis='both', which='both', bottom=True, top=False,
    labelbottom=True, left=False, right=False, labelleft=True)

    return fig, ax

def plot_b_converging(b_converging):
    '''
    Plot the data each user is trying to offload till convergence

    Parameters
    ----------

    b_converging: 2-d array
        Contains on each row the amount of data each user is trying to offload. Each row is
        a different iteration

    Returns
    -------

    Plot

    '''
    result = b_converging

    # Each row on the transposed matrix contains the data the user offloads
    # in each iteration. Different rows mean different user.
    result = np.transpose(result)

    suptitle = "Data each user is trying to offload in each iteration"

    if ONE_FIGURE == False:
        fig, ax = setup_plots(suptitle)

    for index, row in enumerate(result):
        # # display only some of the users on the plot
        # if index%11 == 0:
        #     line = plt.plot(row, lw=5)
        line = plt.plot(row, lw=5)

    average = np.mean(result, axis=0)
    line = plt.plot(average, '--', lw=5, color='black')

    plt.xlabel('iterations', fontweight='bold')
    plt.ylabel('amount of data (bytes)', fontweight='bold')

    path_name = "b_converging"
    if SAVE_FIGS == True and ONE_FIGURE == False:
        plt.savefig("plots/" + path_name + ".png")
    else:
        plt.show(block=False)

def plot_expected_utility_converging(expected_utility_converging):
    '''
    Plot the expected utility of each user till convergence

    Parameters
    ----------

    expected_utility_converging: 2-d array
        Contains on each row the expected utility of each user. Each row is
        a different iteration

    Returns
    -------

    Plot

    '''
    result = expected_utility_converging

    # Each row on the transposed matrix contains the data the user offloads
    # in each iteration. Different rows mean different user.
    result = np.transpose(result)

    suptitle = "Expected utility of each user in each iteration"

    if ONE_FIGURE == False:
        fig, ax = setup_plots(suptitle)

    for index, row in enumerate(result):
        # # display only some of the users on the plot
        # if index%11 == 0:
        #     line = plt.plot(row, lw=5)
        line = plt.plot(row, lw=5)

    average = np.mean(result, axis=0)
    line = plt.plot(average, '--', lw=5, color='black')

    plt.xlabel('iterations', fontweight='bold')
    plt.ylabel('expected utility', fontweight='bold')

    path_name = "expected_utility"
    if SAVE_FIGS == True and ONE_FIGURE == False:
        plt.savefig("plots/" + path_name + ".png")
    else:
        plt.show(block=False)

def plot_pricing_converging(pricing_converging):
    '''
    Plot the pricing set for each user till convergence

    Parameters
    ----------

    pricing_converging: 2-d array
        Contains on each row the pricing for each user. Each row is
        a different iteration

    Returns
    -------

    Plot

    '''
    result = pricing_converging

    # Each row on the transposed matrix contains the data the user offloads
    # in each iteration. Different rows mean different user.
    result = np.transpose(result)

    suptitle = "Pricing each user in each iteration"

    if ONE_FIGURE == False:
        fig, ax = setup_plots(suptitle)

    for index, row in enumerate(result):
        # # display only some of the users on the plot
        # if index%11 == 0:
        #     line = plt.plot(row, lw=5)
        line = plt.plot(row, lw=5)

    average = np.mean(result, axis=0)
    line = plt.plot(average, '--', lw=5, color='black')

    plt.xlabel('iterations', fontweight='bold')
    plt.ylabel('pricing', fontweight='bold')

    path_name = "pricing"
    if SAVE_FIGS == True and ONE_FIGURE == False:
        plt.savefig("plots/" + path_name + ".png")
    else:
        plt.show(block=False)

def plot_PoF_converging(PoF_converging):
    '''
    Plot the probability of failure of MEC server till convergence

    Parameters
    ----------

    PoF_converging: 1-d array
        Contains the probability of failure of the MEC server in each iteration

    Returns
    -------

    Plot

    '''
    result = PoF_converging

    # Each row on the transposed matrix contains the data the user offloads
    # in each iteration. Different rows mean different user.
    result = np.transpose(result)

    suptitle = "Probability of failure of MEC server in each iteration"

    if ONE_FIGURE == False:
        fig, ax = setup_plots(suptitle)

    line = plt.plot(result, lw=5)

    plt.xlabel('iterations', fontweight='bold')
    plt.ylabel('PoF', fontweight='bold')

    path_name = "PoF"
    if SAVE_FIGS == True and ONE_FIGURE == False:
        plt.savefig("plots/" + path_name + ".png")
    else:
        plt.show(block=False)

def plot_explicit_utility_and_pricing_converging(expected_utility_converging, pricing_converging):
    '''
    Plot the average explitic utility and pricing of users till convergence

    Parameters
    ----------

    expected_utility_converging: 2-d array
        Contains on each row the expected utility of each user. Each row is
        a different iteration
    pricing_converging: 2-d array
        Contains on each row the pricing for each user. Each row is
        a different iteration

    Returns
    -------

    Plot

    '''
    result1 = expected_utility_converging
    result2 = pricing_converging

    # Each row on the transposed matrix contains the data the user offloads
    # in each iteration. Different rows mean different user.
    result1 = np.transpose(result1)
    result2 = np.transpose(result2)

    suptitle = "Average expected utility and expected pricing for each user in each iteration"

    if ONE_FIGURE == False:
        fig, ax1 = setup_plots(suptitle)

    average1 = np.mean(result1, axis=0)
    line = plt.plot(average1, lw=5)

    plt.xlabel('iterations', fontweight='bold')
    plt.ylabel('expected utility', fontweight='bold')

    ax2 = ax1.twinx() # instantiate a second axes that shares the same x-axis

    plt.ylabel('pricing', fontweight='bold')

    average2 = np.mean(result2, axis=0)
    line = plt.plot(average2, '--', lw=5, color='black')

    path_name = "explicit_utility_and_pricing"
    if SAVE_FIGS == True and ONE_FIGURE == False:
        plt.savefig("plots/" + path_name + ".png")
    else:
        plt.show(block=False)
