t=int(input())
usersHash={
}
for i in range(t):
    line=input()
    if line in usersHash:
        usersHash[line]+=1
    else:
        usersHash[line]=0
    if usersHash[line]==0:
        print("OK")
    else:
        print(line+str(usersHash[line]))
