from itertools import combinations_with_replacement
n,k=map(str,input().split())
for c in combinations_with_replacement(sorted(n), int(k)):
    print("".join(c))
