a=set(map(int,input().split()))
n=int(input())
k=True
for i in range(n):
    b=set(map(int,input().split()))
    if(a.issuperset(b)==False):
        k=False
print(k)
