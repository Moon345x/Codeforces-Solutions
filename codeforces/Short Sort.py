dic=["abc","bac","acb","cba"]
t=int(input())
while(t>0):
    l=input()
    if l in dic:
        print("YES")
    else:
        print("NO")
    t-=1