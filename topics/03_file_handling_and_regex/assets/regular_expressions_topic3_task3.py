def define_uppercase_followed_by_lowercase(check_str):
    n = range(len(check_str) - 1)
    for i in n:
        if check_str[i].isupper() and check_str[i + 1].islower():
            return True
    return False

"""
An example
"""
print(define_uppercase_followed_by_lowercase('75serS3'))
print(define_uppercase_followed_by_lowercase('75WseTrS3'))
