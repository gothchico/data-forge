# data forge

data platform

## setup

to get started, clone this repo and set up your environment:

1. **clone the repository**

   ```bash
   git clone <repository-url>
   cd data-forge
   ```

2. **set up the conda environment**

   install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **add the root directory to python path**

   ensure all imports work correctly by adding the project root to your `pythonpath`:

   - **setting pythonpath manually**  
     set `pythonpath` manually:
     ```bash
     export PYTHONPATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
     ```

## usage

### running simulations

to try out a simulation of the platform, run:

```bash
python test/integration-test/simulation.py
```

this will generate some sample data, store it in the data lake, add it to the catalog, and run a few transformations and analyses using the main components.

### running unit tests

you can run the unit tests to check that everything’s working as expected:

```bash
python -m unittest discover -s test/unit-test
```

for more detailed output for each test, use:

```bash
python -m unittest discover -s test/unit-test -v
```
