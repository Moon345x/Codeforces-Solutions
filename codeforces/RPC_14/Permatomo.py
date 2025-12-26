t = int(input())
pares = []

for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))

    for j in range(n):
        for y in range(n):
            pares.append(l[j] + l[y])

    pares.sort()
    print(pares[k - 1])
    pares = []
