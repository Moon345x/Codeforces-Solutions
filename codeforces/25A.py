n=int(input())
eveen=0
odd=0
numbers=list(map(int,input().split()))
for i in numbers:

    if i%2==0:
        eveen+=1
    else:
        odd+=1
    if eveen>=2:
        band=True
    if odd>=2:
        band=False
if band:
    for i in numbers:
        if i%2!=0:
            print(numbers.index(i)+1)
            break
else:
    for i in numbers:
        if i%2==0:
            print(numbers.index(i)+1)
            break
