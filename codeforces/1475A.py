t=int(input())
for _ in range(t):
    line=int(input())
    if line&(line-1):
        print("YES")
    else:
        print("NO")
    