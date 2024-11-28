def contains_required_chars(check_str, required_chars):
    """
    Convert both strings to sets of characters
    """
    base_set = set(check_str)
    required_set = set(required_chars)

    """
    Check if all required characters are in the check string
    """
    return required_set.issubset(base_set)


"""
An example
"""
check_string = '7865serS3'

"""
Test scenario
"""
print(contains_required_chars(check_string, '583'))
print(contains_required_chars(check_string, '973'))