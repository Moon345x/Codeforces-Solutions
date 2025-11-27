a=int(input())
b=int(input())
c=int(input())


maxi=1
aux=0
c1=(a+b)*c
c2=a*(b+c)
c3=a+b+c
c4=a*b*c
maxi=max(c1,c2,c3,c4,maxi)
print(maxi)