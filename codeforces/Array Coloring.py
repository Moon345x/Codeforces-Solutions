t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for i in range(n):
        if a[i]%2!=0:
            count+=1
    if count%2==0:
        print("YES")
    else:
        print("NO")
    t-=1