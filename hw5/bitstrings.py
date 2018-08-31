def num_no(n):
    d = {0: 1, 1: 2}  # n: num_of_n-bit_strings_without_00
    return internal_num_no(d, n)

def internal_num_no(d, n):
    if n not in d:
        d[n] = internal_num_no(d, n-1) + internal_num_no(d, n-2)
    return d[n]

def num_yes(n):
    d = {0: 1, 1: 2}  # n: num_of_n-bit_strings_without_00
    return pow(2, n) - internal_num_no(d, n)
