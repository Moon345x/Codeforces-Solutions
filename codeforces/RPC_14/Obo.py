A, X = map(int, input().split())
a = A
aux = 2
cont = 0
ok = True

while aux*aux<=a:
    while a%aux==0:
        cont+=1
        if aux>X:
            ok=False
        a//=aux
    aux+=1
if a>1:
    cont+=1
    if a>X:
        ok=False
if ok:
    print(cont)
else:
    print("what is Obo?")
