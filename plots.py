'''
Plot functions to graphically present simulation results
'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

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
    plt.rc('font', family='serif')
    plt.rc('font', size=44)
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')

    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    # fig.suptitle(suptitle)
    # for item in ([ax.title, ax.xaxis.label, ax.yaxis.label]):
    #     item.set_fontsize(30)
    # for item in (ax.get_xticklabels() + ax.get_yticklabels()):
    #     item.set_fontsize(26)
    #     item.set_fontweight("normal")
    # font = {'weight' : 'normal'}
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
        #     line = plt.plot(row, lw=4)
        line = plt.plot(row, '-', lw=2, color='0.5')

    average = np.mean(result, axis=0)
    line = plt.plot(average, '-', lw=4, color='black')

    plt.xlabel('iterations', fontweight='normal')
    plt.ylabel('Amount of Offloaded Data [bits]', fontweight='normal')

    grey_lines = mlines.Line2D([], [], lw = 2, color='0.5', label='each user')
    black_line = mlines.Line2D([], [], lw = 4, color='k', label='average')
    plt.legend(handles=[grey_lines, black_line], loc=1, prop={'size': 24})

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
        #     line = plt.plot(row, lw=4)
        line = plt.plot(row, '-', lw=2, color='0.5')

    average = np.mean(result, axis=0)
    line = plt.plot(average, '-', lw=4, color='k')

    plt.xlabel('iterations', fontweight='normal')
    plt.ylabel("User's Expected Utility", fontweight='normal')

    grey_lines = mlines.Line2D([], [], lw = 2, color='0.5', label='each user')
    black_line = mlines.Line2D([], [], lw = 4, color='k', label='average')
    plt.legend(handles=[grey_lines, black_line], loc=1, prop={'size': 24})

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

    plt.ticklabel_format(style='sci', axis='y', scilimits=(7,7))

    for index, row in enumerate(result):
        # # display only some of the users on the plot
        # if index%11 == 0:
        #     line = plt.plot(row, lw=4)
        line = plt.plot(row, '-', lw=2, color='0.5')

    average = np.mean(result, axis=0)
    line = plt.plot(average, '-', lw=4, color='k')

    plt.xlabel('iterations', fontweight='normal')
    plt.ylabel('Pricing', fontweight='normal')

    grey_lines = mlines.Line2D([], [], lw = 2, color='0.5', label='each user')
    black_line = mlines.Line2D([], [], lw = 4, color='k', label='average')
    plt.legend(handles=[grey_lines, black_line], loc=1, prop={'size': 24})

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

    line = plt.plot(result, lw=4, color='k')

    plt.xlabel('iterations', fontweight='normal')
    plt.ylabel('PoF', fontweight='normal')

    path_name = "PoF"
    if SAVE_FIGS == True and ONE_FIGURE == False:
        plt.savefig("plots/" + path_name + ".png")
    else:
        plt.show(block=False)

def plot_expected_utility_and_pricing_converging(expected_utility_converging, pricing_converging):
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
        plt.rc('font', family='serif')
        plt.rc('font', size=44)
        plt.rc('xtick', labelsize='x-small')
        plt.rc('ytick', labelsize='x-small')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

        fig = plt.figure(figsize=(16,12))

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.85)

    ax2 = host.twinx() # instantiate a second axes that shares the same x-axis
    ax2.axis["right"].toggle(all=True)
    ax2.ticklabel_format(style='sci', axis='y', scilimits=(7,7))

    average1 = np.mean(result1, axis=0)

    line = host.plot(average1, '--', lw=4, color='k', label='expected utility')

    host.set_xlabel('iterations', fontweight='normal')
    host.set_ylabel('Average Expected Utility', fontweight='normal')

    ax2.set_ylabel('Average Pricing', fontweight='normal')

    average2 = np.mean(result2, axis=0)
    line = ax2.plot(average2, ':', lw=4, color='0.5', label="pricing")

    host.legend(loc=1, prop={'size': 24})

    path_name = "expected_utility_and_pricing"
    if SAVE_FIGS == True and ONE_FIGURE == False:
        plt.savefig("plots/" + path_name + ".png")
    else:
        plt.show(block=False)
