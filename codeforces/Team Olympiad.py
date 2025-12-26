n = int(input().strip())
t = list(map(int, input().split()))

idx1 = []
idx2 = []
idx3 = []

for i, v in enumerate(t, start=1):
    if v == 1:
        idx1.append(i)
    elif v == 2:
        idx2.append(i)
    elif v == 3:
        idx3.append(i)

w = min(len(idx1), len(idx2), len(idx3))
print(w)

for i in range(w):
    print(idx1[i], idx2[i], idx3[i])
