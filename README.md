# Apriori
A Python implementation of the (randomized) Apriori algorithm for mining frequent item sets. 

## Run
The usage of the Apriori implementation as well as a performance comparison of standard Apriori vs. randomized Apriori in the notebook `apriori.ipynb`.

To run the unittests testing different aspects of the program, you can use the commands
```bash
python -m unittest tests.test_shingling
python -m unittest tests.test_minhash # run multiple times due to probabilistic nature
python -m unittest tests.test_LSH
```

## Installation
The required dependencies are specified in the `requirements.txt`. You can install them by running `pip install -r requirements.txt`.

## Generate your own requirements file
The projects uses [pip-tools](https://github.com/jazzband/pip-tools) to generate a requirements file based on the dependencies specified in `pyproject.toml`. To generate your own requirements file (e.g. for a different version of Python) install pip-tools and run
```bash
pip-compile -o requirements.txt pyproject.toml
``` 
