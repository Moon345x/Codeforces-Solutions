# 29/01/26 - codeforces round 1077 div 2
# by juanes_345

def construir(n,band):
    line=""
    aux=int(n/2)+1
    if band:
        line+=str(aux)
        for i in range(1,n):
            if band:
                aux-=i
                band=False
            else:
                aux+=i
                band=True
            line+=" "+str(aux)
    else:
        line+=str(aux)
        for i in range(1,n):
            if band:
                aux-=i
                band=False
            else:
                aux+=i
                band=True
            line+=" "+str(aux)
    return line



t=int(input())
for _ in range(t):
    n=int(input())
    if n==2:
        print("1 2")
    else:
        if n%2==0:
            band=True
        else:
            band=False
        print(construir(n,band))
        

    
        