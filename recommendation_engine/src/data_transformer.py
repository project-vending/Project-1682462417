python
import pandas as pd
import numpy as np

class DataTransformer:
    """
    A class for transforming raw data into the appropriate format for
    the recommendation engine.

    Parameters
    ----------
    user_data: str
        The file path to the user data CSV file.
    item_data: str
        The file path to the item data CSV file.

    Attributes
    ----------
    user_df: pd.DataFrame
        The user data as a Pandas DataFrame.
    item_df: pd.DataFrame
        The item data as a Pandas DataFrame.
    user_product_matrix: np.ndarray
        The user-product interaction matrix as a NumPy array.
    """

    def __init__(self, user_data, item_data):
        self.user_data = user_data
        self.item_data = item_data

        self.user_df = pd.read_csv(self.user_data)
        self.item_df = pd.read_csv(self.item_data)

        self.user_product_matrix = None

    def transform_data(self):
        """
        Transform the raw data into the appropriate format for the recommendation
        engine. The user-product interaction matrix is created with users as rows
        and products as columns, where the values are 1 if the user has interacted
        with the product and 0 otherwise.

        Returns
        -------
        None
        """
        # Combine the user and item data
        combined_df = pd.merge(self.user_df, self.item_df, on='item_id')

        # Create the user-product interaction matrix
        self.user_product_matrix = combined_df.pivot_table(
            values='interaction',
            index='user_id',
            columns='item_id',
            fill_value=0
        ).values
