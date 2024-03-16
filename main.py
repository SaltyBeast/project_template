from app.io import output, input


def main():
    print("Write/read data with built in functionality")
    user_input = input.console_input()
    print("User input: ", user_input)
    output.write_file_builtin("data/built_in_file.txt", user_input)
    print("Text was written in the file")
    file_content = input.read_file_builtin("data/built_in_file.txt")
    print("File content: ", file_content)

    print("Read data with functionality from Pandas")
    file_content = input.read_file_pandas("data/built_in_file.txt")
    print("File content: ", file_content)


if __name__ == "__main__":
    main()
