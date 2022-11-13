def BMS_compare(a, b):
    for i in range(len(a)):
        if a[i] != b[i]: return a[i] < b[i]
    return False

def BMS_expand(seq, n):
    # rule 1 not included
    if all(i == 0 for i in seq[-1]): return seq[:-1] # rule 2
    # rule 3.1