n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

passed_levels = set(x[1:] + y[1:])

if len(passed_levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")