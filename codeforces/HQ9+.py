l=input()
dic=['H','Q','9']
band=False
for i in l:
    if i in dic:
        band=True
        break
if band:
    print("YES")
else:
    print("NO")