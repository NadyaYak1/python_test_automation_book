def read_files(input):
    try:
        """
        Read all lines from the input file
        """
        with open(input, 'r') as file:
            text = file.readlines()
            return text

    except FileNotFoundError:
        print(f"The file '{input}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_words_of_length(text, n):
    try:
        """
        create text from input file
        """
        lines = ' '.join(text)
        """
        Split the text into words
        """
        words = lines.split()


        """
        Filter words of the specified length
        """
        filtered_words = [word for word in words if len(word) == n]

        print(f"Words with {n} characters:")
        for word in filtered_words:
            print(word)
    except Exception as e:
        print(f"An error occurred: {e}")


"""
An example
"""
input_file = "file1_topic3_task2.txt"
n = 3
input_text = read_files(input_file)
print_words_of_length(input_text, n)
