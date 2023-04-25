python
import pandas as pd


def load_user_data(filepath):
    """Load user data from a CSV file and return as a pandas DataFrame"""
    return pd.read_csv(filepath)


def load_item_data(filepath):
    """Load item data from a CSV file and return as a pandas DataFrame"""
    return pd.read_csv(filepath)
