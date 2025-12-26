t=int(input())
answers = []
for _ in range(t):
    n,k=map(int,input().split())
    if k % 2 == 1:
        ans = [n] * k
    else:
        ans = [n, 0] + [n] * (k - 2)
    answers.append(' '.join(map(str, ans)))

print('\n'.join(answers))