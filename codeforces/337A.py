n,m=map(int,input().split())
puzzles=list(map(int,input().split()))
puzzles.sort()
mindif=maxint=10**9
last=n-1
init=0
rou=0
band=True
while(True):
    if m==2:
        mindif=min(mindif,puzzles[last]-puzzles[init])
        break
    if last==m-1:
        band=False
    mindif=min(mindif,puzzles[last]-puzzles[init])
    last+=1
    init+=1
    rou+=1
    if band==False:
        break
print(mindif)