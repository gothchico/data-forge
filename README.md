data forge

data platform

setup
to get started, clone this repo and set up your environment:

clone the repo

bash
Copy code
git clone <repository-url>
cd data-forge
set up the conda environment install the required dependencies:

bash
Copy code
pip install -r requirements.txt
add the root directory to python path

make sure everything can import correctly by adding the project root to your PYTHONPATH:

bash
Copy code
chmod +x ./setup.sh
./setup.sh
or you can set PYTHONPATH manually if you prefer:

bash
Copy code
export PYTHONPATH="/path/to/data-forge"
usage
running simulations
to try out a simulation of the platform, run:

bash
Copy code
python test/integration-test/simulation.py
this will generate some sample data, store it in the data lake, add it to the catalog, and run a few transformations and analyses using the main components.

running unit tests
you can run the unit tests to check that everything’s working as expected:

bash
Copy code
python -m unittest discover -s test/unit-test
for a bit more detail on each test, use:

bash
Copy code
python -m unittest discover -s test/unit-test -v
