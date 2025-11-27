n=int(input())
l=input().split()
l=[int(i) for i in l]
l_sort=sorted(l)
strng=''
for i in l_sort:
    strng+=str(i)+" "
strng=strng.rstrip()
print(strng)