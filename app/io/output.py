import pandas as pd


def output_console(text):
    """
    Prints the text as parameter to the console

    Examples:
        >>> output_console("hello")
        hello

    Args:
        text (str): The text to be printed.

    Returns:
        None
    """
    print(text)


def write_file_builtin(file_name, text):
    """
    Writes text to a file using
    the built-in Python function

    Examples:
        >>> write_file_builtin("../../data/test.txt", "hello")

    Args:
        file_name (str): Path to the file to write to.
        text (str): The content to write to the file.

    Returns:
        None
    """
    with open(file_name, "w") as file:
        file.write(text)


def write_file_pandas(file_name, text):
    """
    Writes text to a file using
    the Pandas function

    Examples:
        >>> write_file_pandas("../../data/pandas_file.csv", "hello")

    Args:
        file_name (str): Path to the file to write to.
        text (str): The content to write to the file.

    Returns:
        None
    """
    write_data = {
        "content": [text]
    }
    df = pd.DataFrame(write_data)
    df.to_csv(file_name)
