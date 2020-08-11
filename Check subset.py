t=int(input())
for i in range(t):
    l=int(input())
    m=list(map(int,input().split()))
    n=int(input())
    o=list(map(int,input().split()))
    p=0
    for i in m:
        if i in o:
            p=p+1
    if p==l:
        print("True")
    else:
        print("False")
