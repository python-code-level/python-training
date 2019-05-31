Developers Setup Guide
======================

Change directory to where your project repo will be located 

e.g. 

``cd GitHub-repos``


Windows terminal (manual, with verification)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:: Verify appropriate python version in insallted (>= 3.6.7) 

``python --version``

:: Clone the repo content from remote GitHub repo

``git clone https://github.com/python-code-level/python-training.git``

:: Create a new virtualenv within the repo 

``py -m venv env``

:: Verify creation of the virtual env

``dir``

:: Activate the virtualenv

``cd env/Scripts
  activate.bat``

:: Return to repo root

``cd ../..``

:: Install required packages

``pip install -r requirements.txt``


Linux terminal (manual, with verification)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Verify appropriate python version in insallted (>= 3.6.7) 

``python --version``

# Clone the repo content from remote GitHub repo

``git clone https://github.com/python-code-level/python-training.git``

# Create a new virtualenv within the repo 

``python3 -m venv env``

# Verify creation of virtual env

``ll``

# Activate the virtualenv

``source env/bin/activate``

# Install required packages

``pip install -r requirements.txt``

