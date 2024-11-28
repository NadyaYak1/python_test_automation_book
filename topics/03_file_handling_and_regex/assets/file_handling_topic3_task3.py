def combine_files(file1, file2, output_file):
    try:
        """
        Read a text from file1
        """
        with open(file1, 'r') as f1:
            x = f1.read()

        """
        Read a text from file2
        """
        with open(file2, 'r') as f2:
            y = f2.read()

        """
        Open the output file in write mode, and write the info from the file1 and file2
        """
        with open(output_file, 'w') as outfile:
            outfile.write(x)
            outfile.write('\n\n')
            outfile.write(y)

        print(f"Contents of '{file1}' and '{file2}' have been combined into '{output_file}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

"""
An example
"""
file_1 = "file1_topic3_task3.txt"
file_2 = "file2_topic3_task3.txt"
output_file = "combined_file_topic3.txt"

combine_files(file_1, file_2, output_file)

