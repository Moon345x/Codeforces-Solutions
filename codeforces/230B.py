import math
def sieve(n):
    """
    Devuelve una lista booleana is_prime[0..n],
    donde is_prime[x] es True si x es primo.
    """
    is_prime = [True] * (n + 1)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Marcamos todos los múltiplos de p como compuestos
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    return is_prime

N =10**6
is_prime = sieve(N)



n=int(input())
numbers=list(map(int,input().split()))
for i in numbers:
    r=int(math.sqrt(i))
    if r*r==i and is_prime[r]:
        print("YES")
    else:
        print("NO")
