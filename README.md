# Apriori
A Python implementation of the (randomized) Apriori algorithm for mining frequent item sets. 

## Run
The usage of the Apriori implementation as well as a performance comparison of standard Apriori versus randomized Apriori is contained in the notebook `apriori.ipynb`.
## Installation
The required dependencies are 
- `pandas` and
- `matplotlib`
  
as specified in the `requirements.txt`. You can install them manually or by running `pip install -r requirements.txt`.

## Generate your own requirements file
The project uses [pip-tools](https://github.com/jazzband/pip-tools) to generate a requirements file based on the dependencies specified in `pyproject.toml`. To generate your own requirements file (e.g. for a different version of Python) install pip-tools and run
```bash
pip-compile -o requirements.txt pyproject.toml
``` 
