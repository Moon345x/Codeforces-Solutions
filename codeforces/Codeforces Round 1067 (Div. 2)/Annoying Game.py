t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    movs_alice = (k + 1) // 2
    movs_bob = k // 2

    suma_prefijo = [0] * (n + 1)
    for i in range(1, n + 1):
        suma_prefijo[i] = suma_prefijo[i - 1] + a[i - 1]

    valores_b_ordenados = sorted(b, reverse=True)
    suma_b_mejores = [0] * (n + 1)
    for i in range(1, n + 1):
        suma_b_mejores[i] = suma_b_mejores[i - 1] + valores_b_ordenados[i - 1]

    resultado_maximo = float('-inf')

    for i in range(n):
        for j in range(i, n):
            suma_base = suma_prefijo[j + 1] - suma_prefijo[i]
            tamano_subarray = j - i + 1

            movs_comunes = min(movs_alice, movs_bob, tamano_subarray)
            movs_alice_extra = min(movs_alice - movs_bob, tamano_subarray - movs_comunes)

            ganancia_alice = suma_b_mejores[movs_comunes + movs_alice_extra] - suma_b_mejores[movs_comunes]

            resultado_maximo = max(resultado_maximo, suma_base + ganancia_alice)

    print(resultado_maximo)
