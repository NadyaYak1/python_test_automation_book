def count_uppercase_letters(check_str):
    """
    Check every character in the string for uppercase letters
    """
    x = 0
    for char in check_str:
        if char.isupper():
            x += 1
    return x

"""
An Example
"""
check_string1 = '7865serS3'
uppercase_count = count_uppercase_letters(check_string1)
print(f"Number of Capital letters: {uppercase_count}")

check_string2 = '7865serSWddI3'
uppercase_count = count_uppercase_letters(check_string2)
print(f"Number of Capital letters: {uppercase_count}")
