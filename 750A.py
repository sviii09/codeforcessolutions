n, k = map(int, input().split())

time_left = 240 - k
total_time = 0
solved = 0

for i in range(1, n + 1):
    if total_time + 5 * i <= time_left:
        total_time += 5 * i
        solved += 1
    else:
        break

print(solved)