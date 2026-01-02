t=int(input())
for _ in range(t):
    line=input()
    if len(line)==1 and int(line)==6:
        print("YES")
    elif (int(line[0:])/2)%2!=0:
        print("YES")
    elif int(line[len(line)-1]) %2==0:
        print("NO")
    
    else:
        print("YES")