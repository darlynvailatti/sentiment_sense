#!/bin/bash

# Step 1: Install pip if not already installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found, installing..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    rm get-pip.py
else
    echo "pip is already installed"
fi

# Step 2: Install pipenv using pip
pip install pipenv

# Step 3: Install dependencies from Pipfile
pipenv install

# Step 4: Run the Flask app
pipenv run python app/app.py