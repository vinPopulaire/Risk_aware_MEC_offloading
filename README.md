# Pricing_aware
Code for generating Pricing_aware_offloading paper's simulation results.

### Abstract

Put abstract here when paper is ready

### Prerequisites

Clone the repository locally
```
git clone https://github.com/vinPopulaire/Pricing_aware_offloading.git
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

Create folders inside project root folder to store paramters and results
```
mkdir runs runs/parameters runs/results
```

### Run simulations

Set general parameters of the simulation
```
vim paremeters.py
```

Set cases to run and number of repetitions of the simulation
```
vim simulations.py
```

Run simulation
```
ipython simulation.py
```

## Authors

* **Giorgos Mitsis** - [vinpopulaire](https://github.com/vinPopulaire)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
