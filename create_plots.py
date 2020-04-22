import dill
import numpy as np
import pprint

from plots import *
from cycler import cycler
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

def plot_b_constant_all(b_constant_all, params):
    '''
    Plot the data each user is trying to offload till convergence

    Parameters
    ----------

    b_till_convergence: 2-d array
    Contains on each row the amount of data each user is trying to offload. Each row is
    a different iteration

    Returns
    -------
    Plot

    '''
    result = b_constant_all

    # Each row on the transposed matrix contains the data the user offloads
    # in each iteration. Different rows mean different user.
    result = np.transpose(result)

    suptitle = "Expected utility when everybody is offloading a constant amount of data"

    if params["ONE_FIGURE"] == False:
        fig, ax = setup_plots(suptitle)

    for index, row in enumerate(result):
        # # display only some of the users on the plot
        # if index%11 == 0:
        #     line = plt.plot(row, lw=4)
        line = plt.plot(row, lw=1)

    plt.xlabel('Amount of data * 10^6', fontweight='normal')
    plt.ylabel('Expected utility', fontweight='normal')

    path_name = "b_till_convergence"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show()
    plt.savefig("plots/" + path_name + ".png")

def plot_different_c_converging(expected_utility_converging, b_converging, pricing_converging, params):

    suptitle = "Average expected utility, b and pricing"

    if params["ONE_FIGURE"] == False:
        fig, ax1 = setup_plots(suptitle)

    ax1.set_xlabel('iterations', fontweight='normal')
    ax1.set_ylabel('expected utility', fontweight='normal')

    ax2 = ax1.twinx() # instantiate a second axes that shares the same x-axis
    ax3 = ax1.twinx() # instantiate a third axes that shares the same x-axis

    ax2.set_ylabel('b', fontweight='normal')
    ax3.set_ylabel('pricing', fontweight='normal')

    ax1.set_prop_cycle(cycler('color', ['b','g','r']))
    ax2.set_prop_cycle(cycler('color', ['b','g','r']))
    ax3.set_prop_cycle(cycler('color', ['b','g','r']))

    for i in range(len(expected_utility_converging)):
        result1 = expected_utility_converging[i]
        result2 = b_converging[i]
        result3 = pricing_converging[i]

        result1 = np.transpose(result1)
        result2 = np.transpose(result2)
        result3 = np.transpose(result3)

        expected_utility_converging[i] = np.mean(result1, axis=0)
        line = ax1.plot(expected_utility_converging[i], '-', lw=4)

        b_converging[i] = np.mean(result2, axis=0)
        line = ax2.plot(b_converging[i], '--', lw=4)

        pricing_converging[i] = np.mean(result3, axis=0)
        line = ax3.plot(pricing_converging[i], ':', lw=4)

    path_name = "different_c_converging"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show()
    plt.savefig("plots/" + path_name + ".png")

def plot_different_c_b_converging(b_converging, params):

    suptitle = "b converging for different c"

    if params["ONE_FIGURE"] == False:
        fig, ax1 = setup_plots(suptitle)

    ax1.set_xlabel('iterations', fontweight='normal')
    ax1.set_ylabel('offloading data', fontweight='normal')

    ax1.set_prop_cycle(cycler('color', ['b','g','r']))

    for i in range(len(b_converging)):
        result1 = b_converging[i]

        result1 = np.transpose(result1)

        b_converging[i] = np.mean(result1, axis=0)
        line = ax1.plot(b_converging[i], '--', lw=1)

    path_name = "different_c_b_converging"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show()
    plt.savefig("plots/" + path_name + ".png")

def plot_different_kn(kns, b, PoF, params):

    # colors = ['k', 'k']
    colors = ['royalblue', 'k']

    plt.rc('font', family='serif')
    plt.rc('font', size=44)
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)

    suptitle = "Average b and PoF"

    fig = plt.figure(figsize=(16,12))
    # fig.suptitle(suptitle)

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.85)
    plt.subplots_adjust(left=0.2)

    par1 = host.twinx() # instantiate a second axes that shares the same x-axis

    par1.axis["right"].toggle(all=True)

    host.ticklabel_format(style='sci', axis='y', scilimits=(7,7), useMathText=True)

    host.set_xlabel('Loss aversion index k\u2099')
    host.set_ylabel('Average Offloaded Data')
    par1.set_ylabel('Probability of Failure')

    result1 = b
    result2 = PoF

    result1 = np.transpose(result1)

    b = np.mean(result1, axis=0)
    line1, = host.plot(kns, b, '-', lw=4, label="offloading data", color=colors[0])

    line2, = par1.plot(kns, PoF, '--', lw=4, label="PoF", color=colors[1])

    # host.axis["left"].label.set_color(line1.get_color())
    # par1.axis["right"].label.set_color(line2.get_color())
    # par2.axis["right"].label.set_color(line3.get_color())

    host.legend(loc=1, prop={'size': 24})

    path_name = "different_kn"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show()
    plt.savefig("plots/" + path_name + ".png")

def plot_different_an(ans, b, PoF, params):

    # colors = ["k", "k"]
    line_types = ['-', '--']
    colors = ["royalblue", "k"]

    plt.rc('font', family='serif')
    plt.rc('font', size=44)
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    suptitle = "Average b and PoF"

    fig = plt.figure(figsize=(16,12))
    # fig.suptitle(suptitle)

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.85)
    plt.subplots_adjust(left=0.2)

    par1 = host.twinx() # instantiate a second axes that shares the same x-axis

    par1.axis["right"].toggle(all=True)

    host.ticklabel_format(style='sci', axis='y', scilimits=(7,7), useMathText=True)

    host.set_xlabel('Sensitivity α\u2099')
    host.set_ylabel('Average Offloaded Data')
    par1.set_ylabel('Probability of Failure')

    result1 = b
    result2 = PoF

    result1 = np.transpose(result1)

    b = np.mean(result1, axis=0)
    line1, = host.plot(ans, b, line_types[0], lw=4, label="offloading data", color=colors[0])

    line2, = par1.plot(ans, PoF, line_types[1], lw=4, label="PoF", color=colors[1])

    # host.axis["left"].label.set_color(line1.get_color())
    # par1.axis["right"].label.set_color(line2.get_color())
    # par2.axis["right"].label.set_color(line3.get_color())

    host.legend(loc=2, prop={'size': 24})

    path_name = "different_an"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show()
    plt.savefig("plots/" + path_name + ".png")

def plot_different_c(cs, expected_utility, b, pricing, params):

    # colors = ['k','0.7','0.5']
    # line_types = ['--', '-', ':']
    colors = ['darkorange','royalblue','darkgreen']
    line_types = ['-', '-', '-']

    plt.rc('font', family='serif')
    plt.rc('font', size=44)
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    suptitle = "Average expected utility, b and pricing"

    fig = plt.figure(figsize=(16,12))
    # fig.suptitle(suptitle)

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx() # instantiate a second axes that shares the same x-axis
    par2 = host.twinx() # instantiate a third axes that shares the same x-axis

    par1.axis["right"].toggle(all=True)

    offset = 160
    new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    par2.axis["right"] = new_fixed_axis(loc="right",
                                        axes=par2,
                                        offset=(offset, 0))

    par2.axis["right"].toggle(all=True)

    par1.ticklabel_format(style='sci', axis='y', scilimits=(7,7), useMathText=True)
    par2.ticklabel_format(style='sci', axis='y', scilimits=(7,7), useMathText=True)

    host.set_xlabel('Pricing Factor')
    host.set_ylabel('Average Expected Utility')
    par1.set_ylabel('Average Offloaded Data')
    par2.set_ylabel('Average Pricing')

    result1 = expected_utility
    result2 = b
    result3 = pricing

    result1 = np.transpose(result1)
    result2 = np.transpose(result2)
    result3 = np.transpose(result3)

    expected_utility = np.mean(result1, axis=0)
    line1, = host.plot(cs, expected_utility, line_types[0], lw=4, label="expected utility", color=colors[0])

    b = np.mean(result2, axis=0)
    line2, = par1.plot(cs, b, line_types[1], lw=4, label="data", color=colors[1])

    pricing = np.mean(result3, axis=0)
    line3, = par2.plot(cs, pricing, line_types[2], lw=4, label="pricing", color=colors[2])

    # host.axis["left"].label.set_color(line1.get_color())
    # par1.axis["right"].label.set_color(line2.get_color())
    # par2.axis["right"].label.set_color(line3.get_color())

    host.legend(loc=1, prop={'size': 24})

    path_name = "different_c"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show()
    plt.savefig("plots/" + path_name + ".png")

def plot_different_N(Ns, expected_utility, b, pricing, params):

    # colors = ['k','0.7','0.5']
    # line_types = ['--', '-', ':']
    colors = ['darkorange','royalblue','darkgreen']
    line_types = ['-', '-', '-']

    plt.rc('font', family='serif')
    plt.rc('font', size=44)
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    suptitle = "Average expected utility, b and pricing"

    fig = plt.figure(figsize=(15,12))
    # fig.suptitle(suptitle)

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx() # instantiate a second axes that shares the same x-axis
    par2 = host.twinx() # instantiate a third axes that shares the same x-axis

    par1.axis["right"].toggle(all=True)

    offset = 160
    new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    par2.axis["right"] = new_fixed_axis(loc="right",
                                        axes=par2,
                                        offset=(offset, 0))

    par2.axis["right"].toggle(all=True)

    par1.ticklabel_format(style='sci', axis='y', scilimits=(7,7), useMathText=True)
    par2.ticklabel_format(style='sci', axis='y', scilimits=(7,7), useMathText=True)

    host.set_xlabel('Number of Users')
    host.set_ylabel('Average Expected Utility')
    par1.set_ylabel('Average Offloaded Data')
    par2.set_ylabel('Average Pricing')

    result1 = expected_utility
    result2 = b
    result3 = pricing

    result1 = np.transpose(result1)
    result2 = np.transpose(result2)
    result3 = np.transpose(result3)

    # expected_utility = np.mean(result1, axis=0)
    line1, = host.plot(Ns, expected_utility, line_types[0], lw=4, label="expected utility", color=colors[0])

    # b = np.mean(result2, axis=0)
    line2, = par1.plot(Ns, b, line_types[1], lw=4, label="data", color=colors[1], alpha=0.7)

    # pricing = np.mean(result3, axis=0)
    line3, = par2.plot(Ns, pricing, '--', lw=4, label="pricing", color=colors[2])

    # host.axis["left"].label.set_color(line1.get_color())
    # par1.axis["right"].label.set_color(line2.get_color())
    # par2.axis["right"].label.set_color(line3.get_color())

    host.legend(loc=1, prop={'size': 24})

    path_name = "different_N"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show()
    plt.savefig("plots/" + path_name + ".png")

def plot_different_N_b_converging(Ns, b_converging, params):

    suptitle = "j converging for different number of users"

    if params["ONE_FIGURE"] == False:
        fig, ax1 = setup_plots(suptitle)

    ax1.set_xlabel('iterations', fontweight='normal')
    ax1.set_ylabel('Average Offloading Data', fontweight='normal')

    colors = ['k', '0.3', '0.4', '0.5','0.55','0.6','0.7','0.8']

    for i in range(len(b_converging)):
        result1 = b_converging[i]

        result1 = np.transpose(result1)

        b_converging[i] = np.mean(result1, axis=0)
        line = ax1.plot(b_converging[i], '-', lw=4, color=colors[i])

        plt.text(len(b_converging[i]) + 2, b_converging[i][-1], "N = " + str(Ns[i]), fontsize=24)

    plt.ticklabel_format(style='sci', axis='y', scilimits=(7,7), useMathText=True)

    path_name = "different_N_b_converging"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show()
    plt.savefig("plots/" + path_name + ".png")

def plot_different_N_FuC(Ns, PoF, params):

    suptitle = "FuC"

    if params["ONE_FIGURE"] == False:
        fig, ax = setup_plots(suptitle)

    FuC = PoF/PoF[0]

    line = plt.plot(Ns, FuC, '--', lw=4, color='black')

    plt.xlabel('Number of Users', fontweight='normal')
    plt.ylabel('FuC', fontweight='normal')

    path_name = "FuC_vs_N"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show(block=False)
    plt.savefig("plots/" + path_name + ".png")

def plot_different_N_an_FuC(ans, Ns, PoFs, params):

    suptitle = "FuC"

    # colors = ["0.2", "0.2", "0.2"]
    colors = ["indianred", "brown", "darkred"]
    lines = ["-", "-", "-"]
    marker = ["o", "v", "s"]
    labels = ["α\u2099 = 0.2", "α\u2099 = 0.5", "α\u2099 = 0.8"]

    if params["ONE_FIGURE"] == False:
        fig, ax = setup_plots(suptitle)

    for index, an in enumerate(ans):

        FuC = PoFs[index]/PoFs[index][0]

        line = plt.plot(Ns, FuC, lines[index], marker=marker[index], markersize=14, label=labels[index] ,lw=4, color=colors[index])

    plt.xlabel('Number of Users', fontweight='normal')
    plt.ylabel('FuC', fontweight='normal')

    plt.legend(loc=4, prop={'size': 24})

    # current_handles, current_labels = plt.gca().get_legend_handles_labels()

    # # sort or reorder the labels and handles
    # reversed_handles = list(reversed(current_handles))
    # reversed_labels = list(reversed(current_labels))

    # # call plt.legend() with the new values
    # plt.legend(reversed_handles,reversed_labels, loc=2, prop={'size': 24})

    path_name = "FuC_vs_N_ans"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show(block=False)
    plt.savefig("plots/" + path_name + ".png")

def plot_different_N_kn_FuC(kns, Ns, PoFs, params):

    suptitle = "FuC"

    # colors = ['0.2', '0.2', '0.2']
    marker = ["o", "v", "s"]
    colors = ['limegreen', 'forestgreen', 'darkgreen']
    lines = ["-", "-", "-"]
    labels = ["k\u2099 = 0.8", "k\u2099 = 1.2", "k\u2099 = 2.0"]

    if params["ONE_FIGURE"] == False:
        fig, ax = setup_plots(suptitle)

    for index, an in enumerate(kns):

        FuC = PoFs[index]/PoFs[index][0]

        line = plt.plot(Ns, FuC, lines[index], marker=marker[index], markersize=14, label=labels[index] ,lw=4, color= colors[index])

    plt.xlabel('Number of Users', fontweight='normal')
    plt.ylabel('FuC', fontweight='normal')

    plt.legend(loc=4, prop={'size': 24})

    path_name = "FuC_vs_N_kns"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show(block=False)
    plt.savefig("plots/" + path_name + ".png")

def plot_different_c_PoF(cs, PoF, params):

    suptitle = "PoF"

    if params["ONE_FIGURE"] == False:
        fig, ax = setup_plots(suptitle)

    line = plt.plot(cs, PoF, '--', lw=4, color='black')

    plt.xlabel('Pricing Factor', fontweight='normal')
    plt.ylabel('PoF', fontweight='normal')

    path_name = "PoF_vs_cost"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show(block=False)
    plt.savefig("plots/" + path_name + ".png")

def plot_different_an_PoF(ans, PoF, params):

    suptitle = "PoF"

    if params["ONE_FIGURE"] == False:
        fig, ax = setup_plots(suptitle)

    line = plt.plot(ans, PoF, '--', lw=4, color='black')

    plt.xlabel('Sensitivity α\u2099')
    plt.ylabel('PoF', fontweight='normal')

    path_name = "PoF_vs_an"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show(block=False)
    plt.savefig("plots/" + path_name + ".png")

def plot_different_kn_PoF(kns, PoF, params):

    suptitle = "PoF"

    if params["ONE_FIGURE"] == False:
        fig, ax = setup_plots(suptitle)

    line = plt.plot(kns, PoF, '--', lw=4, color='black')

    plt.xlabel('Sensitivity k\u2099', fontweight='normal')
    plt.ylabel('PoF', fontweight='normal')

    path_name = "PoF_vs_kn"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show(block=False)
    plt.savefig("plots/" + path_name + ".png")

def plot_different_offloading(offloadings, energy, params):

    suptitle = "different offloading energies"

    if params["ONE_FIGURE"] == False:
        fig, ax = setup_plots(suptitle)

    result = energy
    result = np.transpose(result)
    mean_energy = np.mean(result, axis=0)

    x = np.arange(len(offloadings))

    plt.bar(x, mean_energy, color='0.3')

    labels = ["only local", "50-50", "only server", "dynamic"]
    plt.xticks(x, labels)

    plt.xlabel('Offloading Mechanism', fontweight='normal')
    plt.ylabel('Energy [joules]', fontweight='normal')

    path_name = "offloading_energy_bars"
    # if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
    #     plt.savefig("plots/" + path_name + ".png")
    # else:
    #     plt.show(block=False)
    plt.savefig("plots/" + path_name + ".png")

case = {"users": "homo"}

##### PLOT DIFFERENT an #####

repetition = 0
expected_utility_converging = []
b_converging = []
pricing_converging = []

expected_utility = []
b = []
pricing = []
PoF = []

N = 25
ans = np.linspace(0.1,1,10)
kn = 1.2
c = 0.5
for an in ans:
    infile = 'saved_runs/results/individual/different an/' + case["users"] + "_N_" + str(N) + "_an_" + str(round(an,3)) + "_kn_" + str(kn) + "_c_" + str(round(c,3)) + "_" + str(repetition)
    with open(infile, 'rb') as in_strm:
        kati = dill.load(in_strm)
        expected_utility.append(kati["expected_utility"].copy())
        b.append(kati["b"].copy())
        pricing.append(kati["pricing"].copy())
        PoF.append(kati["PoF"].copy())
        expected_utility_converging.append(kati["expected_utility_converging"].copy())
        b_converging.append(kati["b_converging"].copy())
        pricing_converging.append(kati["pricing_converging"].copy())

        params = kati["params"]
plot_different_an(ans, b, PoF, params)

##### PLOT DIFFERENT kn #####

repetition = 0
expected_utility_converging = []
b_converging = []
pricing_converging = []

expected_utility = []
b = []
pricing = []
PoF = []

N = 25
an = 0.2
kns = np.linspace(0.2,2,10)
c = 0.5
for kn in kns:
    infile = 'saved_runs/results/individual/different kn/' + case["users"] + "_N_" + str(N) + "_an_" + str(round(an,3)) + "_kn_" + str(round(kn,3)) + "_c_" + str(round(c,3)) + "_" + str(repetition)
    with open(infile, 'rb') as in_strm:
        kati = dill.load(in_strm)
        expected_utility.append(kati["expected_utility"].copy())
        b.append(kati["b"].copy())
        pricing.append(kati["pricing"].copy())
        PoF.append(kati["PoF"].copy())
        expected_utility_converging.append(kati["expected_utility_converging"].copy())
        b_converging.append(kati["b_converging"].copy())
        pricing_converging.append(kati["pricing_converging"].copy())

        params = kati["params"]
plot_different_kn(kns, b, PoF, params)

##### PLOT DIFFERENT N #####

repetition = 0
expected_utility_converging = []
b_converging = []
pricing_converging = []

expected_utility = []
b = []
pricing = []
PoF = []

c = 0.5
an = 0.2
kn = 1.2
# kn = 0.31
Ns = [1,2,5,10,25,50,75,100]

for N in Ns:
    infile = 'saved_runs/results/individual/different N/' + case["users"] + "_N_" + str(N) + "_an_" + str(an) + "_kn_" + str(kn) + "_c_" + str(c) + "_" + str(repetition)
    with open(infile, 'rb') as in_strm:
        kati = dill.load(in_strm)
        # expected_utility_converging.append(kati["expected_utility_converging"].copy())
        # b_converging.append(kati["b_converging"].copy())
        # pricing_converging.append(kati["pricing_converging"].copy())
        expected_utility.append(np.mean(kati["expected_utility"]).copy())
        b.append(np.mean(kati["b"]).copy())
        pricing.append(np.mean(kati["pricing"]).copy())
        PoF.append(kati["PoF"].copy())
        expected_utility_converging.append(kati["expected_utility_converging"].copy())
        b_converging.append(kati["b_converging"].copy())
        pricing_converging.append(kati["pricing_converging"].copy())

        params = kati["params"]
        with open('plots/time', 'a') as f:
            print("N: " + str(kati["N"]) + " -> iterations: " + str(kati["iterations"])+ " -> time: " + str(kati["time"]), file=f)

plot_different_N(Ns, expected_utility, b, pricing, params)
plot_different_N_b_converging(Ns, b_converging, params)
plot_different_N_FuC(Ns, PoF, params)

# plot_b_constant_all(b_constant_all)

##### PLOT DIFFERENT C #####

repetition = 0
expected_utility_converging = []
b_converging = []
pricing_converging = []

expected_utility = []
b = []
pricing = []
PoF = []

N = 25
an = 0.2
kn = 1.2
# kn = 0.31
cs = np.linspace(0.1,0.9,33)
for c in cs:
    infile = 'saved_runs/results/individual/different c/' + case["users"] + "_N_" + str(N) + "_an_" + str(an) + "_kn_" + str(kn) + "_c_" + str(round(c,3)) + "_" + str(repetition)
    with open(infile, 'rb') as in_strm:
        kati = dill.load(in_strm)
        expected_utility.append(kati["expected_utility"].copy())
        b.append(kati["b"].copy())
        pricing.append(kati["pricing"].copy())
        PoF.append(kati["PoF"].copy())
        expected_utility_converging.append(kati["expected_utility_converging"].copy())
        b_converging.append(kati["b_converging"].copy())
        pricing_converging.append(kati["pricing_converging"].copy())

        params = kati["params"]
plot_different_c(cs, expected_utility, b, pricing, params)
plot_different_c_PoF(cs, PoF, params)
# plot_different_c_b_converging(b_converging, params)

##### PLOT different offloading mechanisms #####

repetition = 0
expected_utility_converging = []
b_converging = []
pricing_converging = []

expected_utility = []
b = []
pricing = []
PoF = []

user_energies = []

N = 25
an = 0.2
kn = 1.2
c = 0.5

offloadings = ["_b_constant_0", "_b_constant_0.5", "_b_constant_1", ""]

for offloading in offloadings:
    infile = 'saved_runs/results/individual/different offloading/' + case["users"] + offloading + "_N_" + str(N) + "_an_" + str(an) + "_kn_" + str(kn) + "_c_" + str(round(c,3)) + "_" + str(repetition)
    with open(infile, 'rb') as in_strm:
        kati = dill.load(in_strm)
        expected_utility.append(kati["expected_utility"].copy())
        b.append(kati["b"].copy())
        pricing.append(kati["pricing"].copy())
        PoF.append(kati["PoF"].copy())
        expected_utility_converging.append(kati["expected_utility_converging"].copy())
        b_converging.append(kati["b_converging"].copy())
        pricing_converging.append(kati["pricing_converging"].copy())

        user_energies.append(kati["user_energy"].copy())

        params = kati["params"]
plot_different_offloading(offloadings, user_energies, params)

##### PLOT Pr VS x #####

plt.rc('font', family='serif')
plt.rc('font', size=44)
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')
fig = plt.figure(figsize=(16,12))

# Provide tick lines across the plot to help viewers trace along
# the axis ticks.
plt.grid(True, 'major', 'y', ls='--', lw=.3, c='k', alpha=.3)

# Remove the tick marks; they are unnecessary with the tick lines we just
# plotted.
plt.tick_params(axis='both', which='both', bottom=True, top=False,
    labelbottom=True, left=False, right=False, labelleft=True)
x = np.linspace(0, 10, 10000)
Pr = np.empty_like(x)
dt = np.empty_like(x)
for i in range(len(x)):
    dt[i] = -1 + 2/(1+np.exp(-x[i]))
    Pr[i] = dt[i]**2
plt.xlabel('x')
plt.ylabel('Pr')
plt.plot(x,Pr, color='k')
# if params["SAVE_FIGS"] == True and params["ONE_FIGURE"] == False:
#     plt.savefig("plots/Pr_vs_x.png")
# else:
#     plt.show()
plt.savefig("plots/Pr_vs_x.png")

##### PLOT FuC DIFFERENT N DIFFERENT AN #####

repetition = 0
expected_utility_converging = []
b_converging = []
pricing_converging = []

expected_utility = []
b = []
pricing = []
PoFs = []

c = 0.5
ans = [0.2, 0.5, 0.8]
kn = 1.2
Ns = [1,2,5,10,25,50,75,100]

for an in ans:
    PoF = []
    for N in Ns:
        infile = 'saved_runs/results/individual/different N an/' + case["users"] + "_N_" + str(N) + "_an_" + str(round(an,3)) + "_kn_" + str(kn) + "_c_" + str(c) + "_" + str(repetition)
        with open(infile, 'rb') as in_strm:
            kati = dill.load(in_strm)
            PoF.append(kati["PoF"].copy())

            params = kati["params"]
    PoFs.append(PoF)

plot_different_N_an_FuC(ans, Ns, PoFs, params)

##### PLOT FuC DIFFERENT N DIFFERENT KN #####

repetition = 0
expected_utility_converging = []
b_converging = []
pricing_converging = []

expected_utility = []
b = []
pricing = []
PoFs = []

c = 0.5
an = 0.2
kns = [0.8, 1.2, 2.0]
Ns = [1,2,5,10,25,50,75,100]

for kn in kns:
    PoF = []
    for N in Ns:
        infile = 'saved_runs/results/individual/different N kn/' + case["users"] + "_N_" + str(N) + "_an_" + str(round(an,3)) + "_kn_" + str(round(kn,3)) + "_c_" + str(c) + "_" + str(repetition)
        with open(infile, 'rb') as in_strm:
            kati = dill.load(in_strm)
            PoF.append(kati["PoF"].copy())

            params = kati["params"]
    PoFs.append(PoF)

plot_different_N_kn_FuC(kns, Ns, PoFs, params)

