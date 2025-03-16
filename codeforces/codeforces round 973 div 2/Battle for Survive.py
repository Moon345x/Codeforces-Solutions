t=int(input())
for _ in range(t):
    n=int(input())
    xs=list(map(int,input().split()))
    last=xs[n-1]
    pre_last=xs[n-2]
    xs=xs[:-2]
    suma=0
    for i in xs:
        suma+=i
    pre_last=pre_last-suma
    xd=last-pre_last
    print(xd)

