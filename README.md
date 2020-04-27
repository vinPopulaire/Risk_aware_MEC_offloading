# Risk_aware
Code for generating Data Offloading in UAV-assisted Multi-access Edge Computing Systems: A Resource-based Pricing and User Risk-awareness Approach paper's simulation results. https://www.mdpi.com/1424-8220/20/8/2434/pdf

## Abstract

Unmanned Aerial Vehicle (UAV)-assisted Multi-access Edge Computing (MEC) systems have emerged recently as a flexible and dynamic computing environment, providing task offloading service to the users. In order for such a paradigm to be viable, the operator of a UAV-mounted MEC server should enjoy some form of profit by offering its computing capabilities to the end users. To deal with this issue in this paper, we apply a usage-based pricing policy for allowing the exploitation of the servers’ computing resources. The proposed pricing mechanism implicitly introduces a more social behavior to the users with respect to competing for the UAV-mounted MEC servers' computation resources. In order to properly model the users' risk-aware behavior within the overall data offloading decision-making process the principles of Prospect Theory are adopted, while the exploitation of the available computation resources is considered based on the theory of the Tragedy of the Commons. Initially, the user's prospect-theoretic utility function is formulated by quantifying the user's risk seeking and loss aversion behavior, while taking into account the pricing mechanism. Accordingly, the users' pricing and risk-aware data offloading problem is formulated as a distributed maximization problem of each user's expected prospect-theoretic utility function and addressed as a non-cooperative game among the users. The existence of a Pure Nash Equilibrium (PNE) for the formulated non-cooperative game is shown based on the theory of submodular games. An iterative and distributed algorithm is introduced which converges to the PNE, following the learning rule of the best response dynamics. The performance evaluation of the proposed approach is achieved via modeling and simulation, and detailed numerical results are presented highlighting its key operation features and benefits.

## Prerequisites

Clone the repository locally
```
git clone https://github.com/vinPopulaire/Risk_aware_MEC_offloading.git
```

Create a python virtual environment
```
virtualenv -p python3 env
source env/bin/activate
```

Install dependacies
```
pip install -r requirements.txt
```

Create folders inside project root folder to store parameters and results
```
mkdir saved_runs saved_runs/parameters saved_runs/results saved_runs/results/individual
```

(optional) Create subfolders inside individula runs to store results in such a way that the plot function to generate the results of the paper works
```
cd saved_runs/results/individual
mkdir different\ an different\ c different \kn different\ N different\ N\ an different\ N\ kn different\ offloading different\ type
```

## Run simulations

Set general parameters of the simulation (ATTENTION some of the parameters are redifined inside the simulation.py)
```
vim paremeters.py
```

Run simulation
```
ipython simulation.py
```

## Create plots found in the paper

You can play with the parameters used in the simulation in order to see how the model reacts to changes on each parameter. In order to do so, you can specify the list of values for the specified parameter (or just uncomment the lists provided).
```
vim simulation.py
```

In order to create the plots found in the paper you have to populate the results folders. When a simulation runs, the results are saved inside the results/individual folder. After you run a simulation with a varying parameter, you have to manually move the results inside the corresponding folder.

### Example
If you want to run a simulation with varying costs, you have to:
- set SAVE_PARAMETER = True in parameters.py
- uncomment cpars = np.linspace(0.1,0.9,33) and comment cpars = [0.5] in simulation.py
- run simulation.py
- manually move generated results in saved_runs/results/individual inside the different c folder

After you have created all the needed results, you can run
```
ipython create_plots.py
```
in order to generate the plots.
If not all plots are needed, you have to comment out the part of the function create_plots.py that you don't need

## Authors

* **Giorgos Mitsis** - [vinpopulaire](https://github.com/vinPopulaire)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
