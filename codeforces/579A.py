LIMIT = 10**9

powers_of_two = []
x = 1
while x <= LIMIT:
    powers_of_two.append(x)
    x *= 2

x=int(input())
powers_of_two.sort(reverse=True)
bacteria=0
while x>0:
    for i in powers_of_two:
        if x>=i:
            bacteria+=1
            x-=i
print(bacteria)