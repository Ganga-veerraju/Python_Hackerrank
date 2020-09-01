from itertools import permutations
n,k=map(str,input().split())
a=list(sorted(permutations(n,int(k))))
for i in a:
    print(''.join(i))
