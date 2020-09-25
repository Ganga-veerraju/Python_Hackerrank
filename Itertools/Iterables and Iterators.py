from itertools import combinations
n=int(input())
l=list(map(str,input().split()))
m=int(input())
a=list(combinations(l,m))
count=0
for i in a:
    if 'a' in i:
        count+=1
print(count/len(a))
