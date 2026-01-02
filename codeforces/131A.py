line=list(input())
upers=0
lowers=0
for i in line:
    if i.isupper():
        upers+=1
    else:
        lowers+=1
if upers==len(line):
    print(line[0].upper()+''.join(line[1:]).lower())
elif line[0].islower() and upers==len(line)-1:
    print(line[0].upper()+''.join(line[1:]).lower())
else:
    print(''.join(line))