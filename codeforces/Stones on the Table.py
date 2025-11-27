n=int(input())
l=input().strip()
def quitar_consecutivos(lst):
    if not lst:
        return []
    res = [lst[0]]
    for x in lst[1:]:
        if x != res[-1]:
            res.append(x)
    return res
res=quitar_consecutivos(l)
print(len(l)-len(res))
