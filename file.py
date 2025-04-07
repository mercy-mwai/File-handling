def modify_file_content(content):
    # Example modification: convert all text to uppercase
    return content.upper()

def read_and_write_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read from: ")

        # Open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_file_content(content)

        # Write the modified content to a new file
        new_filename = 'modified_' + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"File successfully modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: There was an issue reading the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()
