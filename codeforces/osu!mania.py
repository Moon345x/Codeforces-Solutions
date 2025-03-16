def posicion(row,n):
    n=n-1
    notes = []
    while n>=0:
        notes.append((row[n].index('#'))+1)
        n-=1
    return notes
t=int(input())
for _ in range(t):
    n=int(input())
    row=[]
    for i in range(n):
        row.append((list(input())))
    print(" ".join(map(str, posicion(row,n))))


