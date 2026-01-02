n,l=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
maxi=a[0]
for i in range(1,n):
    maxi=max((a[i]-a[i-1])/2,maxi)
if a[n-1]!=l:
    maxi=max(maxi,l-a[n-1])
print(maxi)
