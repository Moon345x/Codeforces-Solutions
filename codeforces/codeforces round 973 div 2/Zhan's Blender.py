import math
t=int(input())

for _ in range(t):
    n=int(input())
    x,y=map(int, input().split())
    mini=min(x,y)
    r=math.ceil(n/mini) 
    print(r)