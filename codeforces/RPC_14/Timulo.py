n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = {}

for i in range(n):
    val = v[i]
    col = c[i]

    mejor = 0
    mejor_col = -1

    for col_key, s in dp.items():
        if s > mejor:
            mejor = s
            mejor_col = col_key

    if mejor_col == col and len(dp) > 1:
        mejor = 0
        for col_key, s in dp.items():
            if col_key != col and s > mejor:
                mejor = s

    nueva = mejor + val
    dp[col] = max(dp.get(col, 0), nueva)

print(max(dp.values()) if dp else 0)
