from collections import Counter
t=int(input())
while t>0:
    a,b,c=map(int,input().split())
    list=[a,b,c]
    count=Counter(list)
    for i,j in count.items():
        if j==1:
            print(i)
    t-=1