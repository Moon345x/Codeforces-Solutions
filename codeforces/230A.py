s,n=map(int,input().split())
band=True
dragons=[]
for i in range(n):
    x,y=map(int,input().split())
    dragons.append((x,y))
dragons.sort()
for dragon in dragons:
    if s>dragon[0]:
        s+=dragon[1]
    else:
        band=False
        print("NO")
        break
if band:
    print("YES")
