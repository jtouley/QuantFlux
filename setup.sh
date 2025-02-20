#!/bin/bash

echo "Setting up the Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Installing linting tools and pre-commit hooks..."
pip install black flake8 pre-commit
pre-commit install

echo "Setup complete. Activate the virtual environment using: source venv/bin/activate"
