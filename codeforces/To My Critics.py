t=int(input())
while t:
    a,b,c=map(int,input().split())
    list=[a,b,c]
    list.sort(reverse=True)
    if list[0]+list[1]>=10:
        print("YES")
    else:
        print("NO")
    t-=1