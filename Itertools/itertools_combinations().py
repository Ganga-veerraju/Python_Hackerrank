from itertools import combinations
n,k=map(str,input().split())
for i in range(1, int(k)+1):
    for j in combinations(sorted(n), i):
        print(''.join(j))
