def remove_duplicate_lines(input, output):
    try:
        """
        Read all lines from the input file
        """
        with open(input, 'r') as file:
            lines = file.readlines()

        """
        Remove duplicate lines by converting to a set and preserving the order
        """
        unique_lines = list(dict.fromkeys(lines))

        """
        Write the unique lines to the output file
        """
        with open(output, 'w') as file:
            file.writelines(unique_lines)

        print(f"Duplicates removed. Unique lines are saved in '{output}'.")
    except FileNotFoundError:
        print(f"The file '{input}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

"""
An example
"""
file1_topic3 = "file1_for_topic3.txt"
file2_topic3 = "file2_for_topic3.txt"
remove_duplicate_lines(file1_topic3, file2_topic3)