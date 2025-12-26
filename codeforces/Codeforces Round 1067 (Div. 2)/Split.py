from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    contador = Counter(arr)

    conteo_pares = sum(1 for cnt in contador.values() if cnt % 2 == 0)
    conteo_impares = sum(1 for cnt in contador.values() if cnt % 2 == 1)
    num_distintos = len(contador)

    if conteo_impares >= 1:
        respuesta = num_distintos + conteo_pares
    else:
        desajuste_paridad = (conteo_pares % 2) != (n % 2)
        if desajuste_paridad:
            respuesta = num_distintos + conteo_pares - 2
        else:
            respuesta = num_distintos + conteo_pares

    print(max(0, respuesta))