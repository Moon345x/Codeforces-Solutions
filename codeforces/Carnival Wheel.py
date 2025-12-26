t=int(input())
while t:
    l,a,b=map(int,input().split())
    maxi=-1
    for i in range(l):
        maxi=max(maxi,(a+i*b)%l)
    print(maxi)
    t-=1