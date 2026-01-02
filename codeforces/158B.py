from collections import Counter


n=int(input())
line=list(map(int,input().split()))
numbers=Counter(line)
taxis=0
taxis+=numbers[4]
if numbers[3]>=numbers[1]:
    taxis+=numbers[3]
    numbers[1]=0
    
else:
    taxis+=numbers[3]
    numbers[1]-=numbers[3]
if numbers[2]%2==0:
        taxis+=numbers[2]//2
else: 
    taxis+=numbers[2]//2+1
    numbers[1]-=2
if numbers[1]>0:
    taxis+=numbers[1]//4
    if numbers[1]%4!=0:
        taxis+=1
print(taxis)