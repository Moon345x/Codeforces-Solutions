t=int(input())

while t>0:
    n=int(input())
    y,r=map(int,input().split())
    expulsados=r+int(y/2)
    maxi=expulsados
    if maxi>n:
        mini=n
    else:
        mini=maxi
    print(int(mini))
    t-=1