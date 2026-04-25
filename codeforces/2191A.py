def prueba(l,newdic):
    l.sort()
    bandera=newdic[l[0]]
    for i in range(1,len(l)):
        if newdic[l[i]]=="red" and bandera=="red":
            return False
        if newdic[l[i]]=="blue" and bandera=="blue":
            return False
        bandera=newdic[l[i]]
    return True

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    newdic={}
    band=0
    for i in range(n):
        if band==0:
            newdic[l[i]]="red"
            band=1
        else:
            newdic[l[i]]="blue"
            band=0
    l.sort()
    bandera=newdic[l[0]]
    if prueba(l,newdic):
        print("YES")
    else:
        print("NO")
