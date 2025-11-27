'''import time forma bruta

start = time.perf_counter()  # inicio

n, k = map(int, input().split())
n1 = 1
n2 = 2
cont = 1
lista = [n1]
band = False

# añadir los impares hasta la mitad del numero
while True:
    if cont == k:
        break
    if n1 == n:
        band = True
        break
    if n1 + 1 == n:
        band = True
        break
    n1 += 2
    lista.append(n1)
    cont += 1

if band:
    lista.append(n2)
    cont += 1
    while True:
        if cont == k:
            break
        n2 += 2
        lista.append(n2)
        cont += 1

print(lista[cont-1])

end = time.perf_counter()  # fin
print(f"Tiempo de ejecución: {end - start:.6f} segundos")'''
n,k=map(int,input().split())
mitad=n/2
mitad=mitad.__ceil__()
if k>mitad:
    # es par
    aux=k-mitad
    num=aux*2
else:
    aux=k-1
    num=1+aux*2
print(num)