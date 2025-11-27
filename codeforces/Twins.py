t=input()
l=input().split()
l=[int(i) for i in l]
s=sum(map(int,l))
aux=0
cont=0
l.sort(reverse=True)
for i in l:
    aux+=int(i)
    s-=int(i)
    cont+=1
    if aux>s:
        break

print(cont)