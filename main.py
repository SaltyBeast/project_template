from app.io import output, input


def main():
    output.output_console("Write/read data with built in functionality")
    user_input = input.console_input()
    output.output_console("User input: " + user_input)
    output.write_file_builtin("data/built_in_file.txt", user_input)
    output.output_console("Text was written in the file")

    file_content = input.read_file_builtin("data/built_in_file.txt")
    output.output_console("File content: " + file_content)

    output.output_console("Write/read data with Pandas")
    user_input = input.console_input()
    output.write_file_pandas("data/pandas_file.csv", user_input)
    output.output_console("Read data with functionality from Pandas")
    file_content = input.read_file_pandas("data/pandas_file.csv")
    output.output_console("File content: "+file_content)


if __name__ == "__main__":
    main()
