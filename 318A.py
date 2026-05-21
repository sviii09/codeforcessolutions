n, k = map(int, input().split())

odds_count = (n + 1) // 2

if k <= odds_count:
    print(2 * k - 1)
else:
    print(2 * (k - odds_count))