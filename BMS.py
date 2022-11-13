def BMS_expand(S, n):
    # rule 1 not included
    if all(i == 0 for i in S[-1]): return S[:-1] # rule 2
    