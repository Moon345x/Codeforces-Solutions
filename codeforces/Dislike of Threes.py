list=[]
for i in range(1667):
    if i%3!=0 and i%10!=3:
        list.append(i)
t=int(input())
while t>0:
    k=int(input())
    print(list[k-1])
    t-=1