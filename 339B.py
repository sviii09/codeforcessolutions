n, m = map(int, input().split())
tasks = list(map(int, input().split()))

current_pos = 1
time = 0

for task in tasks:
    if task >= current_pos:
        time += task - current_pos
    else:
        time += n - current_pos + task
    current_pos = task

print(time)