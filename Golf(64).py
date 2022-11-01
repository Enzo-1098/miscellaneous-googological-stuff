def A(a,b,c):return A(a,A(a,b-1,c),c-1) if c>1 else a**b
def G(n):return A(3,3,G(n-1)) if n>1 else A(3,3,4)
print(G(64))