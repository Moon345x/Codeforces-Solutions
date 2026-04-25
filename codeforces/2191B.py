def solve(arr):
    n = len(arr)
    # Prefijos máximos
    prefix_max = [0] * n
    prefix_max[0] = arr[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], arr[i])
    
    # Sufijos máximos
    suffix_max = [0] * n
    suffix_max[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], arr[i])
    
    for i in range(n-1):
        if prefix_max[i] < suffix_max[i+1]:
            return "YES"
    return "NO"
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(solve(arr))