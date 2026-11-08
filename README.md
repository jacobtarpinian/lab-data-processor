# Lab Data Processor

A Python tool that loads experimental lab data from Excel files for analysis.
Built to speed up processing data for my mechanical engineering lab reports.

## Features
- Loads any sheet from an `.xlsx` file
- Lets you choose which row contains the column headers
- Clear error messages for missing files, wrong file types, and invalid sheets

## Requirements
- Python 3.10+
- pandas, openpyxl

## How to run
    git clone https://github.com/jacobtarpinian/lab-data-processor.git
    cd lab-data-processor
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    python main.py

## Planned
- Plotting selected columns
- Curve fitting (e.g. damping ratio from pendulum data)
