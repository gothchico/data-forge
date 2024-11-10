# Data Forge

Data Forge is a data platform that helps manage and analyze different types of data, such as intraday trading data and news sentiment data. It includes features like a data lake, a data catalog, a data workbench, and quantitative data models, allowing you to easily store, retrieve, and transform data.

## Setup

To get started, clone this repo and set up your environment:

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd data-forge
   ```

2. **Set Up the Conda Environment**

   Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Add the Root Directory to Python Path**

   Ensure all imports work correctly by adding the project root to your `PYTHONPATH`:

   - **Using Setup Script**  
     Make the setup script executable and run it:

     ```bash
     chmod +x ./setup.sh
     ./setup.sh
     ```

   - **Setting PYTHONPATH Manually**  
     Alternatively, set `PYTHONPATH` manually:
     ```bash
     export PYTHONPATH="/path/to/data-forge"
     ```

## Usage

### Running Simulations

To try out a simulation of the platform, run:

```bash
python test/integration-test/simulation.py
```

This will generate some sample data, store it in the data lake, add it to the catalog, and run a few transformations and analyses using the main components.

### Running Unit Tests

You can run the unit tests to check that everything’s working as expected:

```bash
python -m unittest discover -s test/unit-test
```

For more detailed output for each test, use:

```bash
python -m unittest discover -s test/unit-test -v
```
