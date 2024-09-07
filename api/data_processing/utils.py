import pandas as pd

def clean_price_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    This function cleans a price column in a pandas DataFrame by:
    1. Treating the column as a string to preserve periods.
    2. Removing periods (.) from the string.
    3. Converting the cleaned string to integers.

    :param df: The pandas DataFrame containing the data.
    :param column_name: The name of the column to clean.
    :return: The DataFrame with the cleaned column.
    """
    df[column_name] = df[column_name].astype(str)  # Convert to string
    df[column_name] = df[column_name].str.replace('.', '', regex=False)  # Remove periods
    df[column_name] = df[column_name].astype(int)  # Convert to integer

    return df

