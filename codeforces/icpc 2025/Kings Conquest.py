def calcular_area(Rmin,Rmax,Cmin,Cmax):
    lado1=abs(Rmin-Rmax)+1
    lado2=abs(Cmin-Cmax)+1
    return lado1*lado2


n,k=map(int,input().split())
Rmin=10**6
Rmax=-10**6
Cmin=10**6
Cmax=-10**6
kings=[]
for i in range(n):
    r,c=map(int,input().split())
    kings.append((r,c))
    Rmin=min(Rmin,r)
    Rmax=max(Rmax,r)
    Cmin=min(Cmin,c)
    Cmax=max(Cmax,c)
areafinal=calcular_area(Rmin,Rmax,Cmin,Cmax)
for r,c in kings:
    #moviendo el rey actual a esquina superior derecha r-k y c+k
    r1=min(Rmin,(r-k))   #r-k
    c1=max(Cmax,c+k)   #c+k
    areafinal=max(areafinal,calcular_area(r1,Rmax,Cmin,c1))
    #movimiendo el reay actual a esquina superior izquierda r-k y c-k
    r2=min(Rmin,r-k)
    c2=min(Cmin,c-k)
    areafinal=max(areafinal,calcular_area(r2,Rmax,c2,Cmax))
    #movimiendo el rey actual a esquina inferior izquierda  r+k y c-k
    r3=max(Rmax,r+k)
    c3=min(Cmin,c-k)
    areafinal=max(areafinal,calcular_area(Rmin,r3,c3,Cmax))
    #moviendo el rey actual a esquina inferior derecha r+k y c+k
    r4=max(Rmax,r+k)
    c4=max(Cmax,c+k)
    areafinal=max(areafinal,calcular_area(Rmin,r4,Cmin,c4))
#ahora vamos a calcular moviendo de otra forma con k movimientos

lado1=abs(Rmin-Rmax)+1
lado2=abs(Cmin-Cmax)+1
diferenciaentrelados=abs(lado1-lado2)
if(k<=diferenciaentrelados):
    if lado1>lado2:
        lado2+=k
    else:
        lado1+=k
else:
    if lado1>lado2:
        lado2+=diferenciaentrelados
    else:
        lado1+=diferenciaentrelados
    Arepartir=k-diferenciaentrelados
    if Arepartir%2==0:
        lado1+=Arepartir//2
        lado2+=Arepartir//2
    else:
        lado1+=Arepartir//2
        lado2+=Arepartir//2
        lado2+=1
posibleareafinal=lado1*lado2
areafinal=max(areafinal,(lado1*lado2))
print(areafinal)
