import pandas as pd


def console_input():
    """
    Get console input and returns the entered value

    Examples:
        >>> console_input()
        Enter some text: hello

    Returns:
        str: The user-entered text.
    """
    user_input = input("Enter some text: ")
    return user_input


def read_file_builtin(file_name):
    """
    Reads the file using the built-in Python function

    Examples:
        >>> read_file_builtin("../../data/test.txt")
        Text from the current fille print in console

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The contents of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(file_name) as file:
        return file.read()


def read_file_pandas(file_name):
    """
    Reads the file using pandas and returns the DataFrame representation.

    Examples:
        >>> read_file_pandas("../../data/pandas_file.csv")
        Dataframe of file

    Args:
        file_name (str): The name of the file to read.

    Returns:
        DataFrame: A DataFrame containing the data from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file format is invalid or cannot be parsed as a DataFrame.
    """
    df = pd.read_csv(file_name)
    return df["content"][0]
