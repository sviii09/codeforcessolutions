t = int(input())
for _ in range(t):
    n = int(input())
    p = [n] + list(range(1, n))
    print(' '.join(map(str, p)))