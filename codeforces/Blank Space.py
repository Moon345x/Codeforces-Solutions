t=int(input())
while t:
    n=int(input())
    aux=0
    maxi=0
    a=list(map(int,input().split()))
    for i in a:
        if i==0:
            aux+=1
        if i==1:
            maxi=max(maxi,aux)
            aux=0
    maxi=max(maxi,aux)
    print(maxi)
    t-=1