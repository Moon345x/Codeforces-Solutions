from itertools import permutations

line = input().strip()
words = input().split()

band = False

for p in permutations(words):
    candidate = "".join(p)
    if candidate in line:
        band = True
        break

if band:
    print("Nooo, la polizzia")
else:
    print("Sargento Camelas, Gracias!")
