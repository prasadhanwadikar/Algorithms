def bsts(n):
    dict = {0: 1} #for memorization
    return internal_bsts(dict, n)

def internal_bsts(dict, n):
    if n not in dict:
        num_of_bsts = 0
        for i in range(1, n + 1):
            num_of_bsts += internal_bsts(dict, i - 1) * internal_bsts(dict, n - i)
        dict[n] = num_of_bsts
    return dict[n]