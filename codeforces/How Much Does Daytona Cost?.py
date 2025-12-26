t=int(input())
while t>0:
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    if k in l:
        print("YES")
    else:
        print("NO")
    t-=1