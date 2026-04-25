t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n==1:
        print(1)
        continue
    ans = s.count('1')
    parts = s.split('1')

    # bloque inicial
    if parts[0]:
        ans += (len(parts[0]) + 1) // 3

    # bloque final
    if len(parts) > 1 and parts[-1]:
        ans += (len(parts[-1]) + 1) // 3

    # bloques intermedios
    for block in parts[1:-1]:
        ans += len(block) // 3

    print(ans)
