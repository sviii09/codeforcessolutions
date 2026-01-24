n, t = map(int, input().split())
queue = list(input())

for _ in range(t):
    i = 0
    while i < n - 1:
        if queue[i] == 'B' and queue[i + 1] == 'G':
            queue[i], queue[i + 1] = 'G', 'B'
            i += 1  # skip next position since it's already swapped
        i += 1

print(''.join(queue))