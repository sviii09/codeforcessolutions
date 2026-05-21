n, l = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

max_gap = 0
for i in range(1, n):
    gap = a[i] - a[i-1]
    if gap > max_gap:
        max_gap = gap

start_gap = a[0] - 0
end_gap = l - a[-1]

radius = max(start_gap, end_gap, max_gap / 2)

print(f"{radius:.10f}")