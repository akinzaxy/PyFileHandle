def read_and_write_file():
    # Ask for the input file name
    input_filename = input("Enter the filename to read from: ")
    output_filename = input("Enter the filename to write to: ")

    try:
        # Try opening the input file
        with open(input_filename, 'r') as infile:
            # Read the contents of the file
            content = infile.read()

        # Modify the content (for this example, convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File has been successfully read from '{input_filename}' and written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: There was an issue reading the file '{input_filename}' or writing to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_and_write_file()
