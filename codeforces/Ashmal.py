t=int(input())
while t:
    n=int(input())
    arr=list(input().split())
    """ord=sorted(arr,key=lambda x: (len(x), x))
    print(ord)"""
    s=""
    for i in arr:
        if s=="":
            s+=i
        else:
            adelante=i+s
            atras=s+i
            if adelante>atras:
                s=atras
            else:
                s=adelante

    print(s)

    t-=1