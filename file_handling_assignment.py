def create_file():
    try:
        # Create a new text file in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("First line\n")
            file.write("Second line\n")
            file.write("12345\n")  # Including a mix of strings and numbers
            print("File created successfully!")
    except IOError as e:
        print("Error: ", e)


def read_and_display_file():
    try:
        # Open the file in read mode
        with open("my_file.txt", "r") as file:
            # Read the contents of the file
            content = file.read()
            # Display the contents on the console
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")


def append_to_file():
    try:
        # Open the file in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("Third line\n")
            file.write("Fourth line\n")
            file.write("54321\n")  # Including a mix of strings and numbers
            print("Data appended to the file successfully!")
    except IOError as e:
        print("Error: ", e)


if __name__ == "__main__":
    # File Creation
    create_file()

    # File Reading and Display
    read_and_display_file()

    # File Appending
    append_to_file()
