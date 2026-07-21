import pandas as pd
import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Path to the data folder
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_csv(filename):
    """
    Load a CSV file from the data folder.
    """

    filepath = os.path.join(DATA_DIR, filename)

    return pd.read_csv(filepath)

def load_transactions():
    return load_csv("transactions.csv")


def load_employees():
    return load_csv("employees.csv")


def load_vendors():
    return load_csv("vendors.csv")


def load_programs():
    return load_csv("programs.csv")


def load_grants():
    return load_csv("grants.csv")


def load_budget():
    return load_csv("budget.csv")

