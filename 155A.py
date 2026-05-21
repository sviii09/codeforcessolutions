n = int(input())
scores = list(map(int, input().split()))

min_score = max_score = scores[0]
amazing_count = 0

for i in range(1, n):
    if scores[i] > max_score:
        max_score = scores[i]
        amazing_count += 1
    elif scores[i] < min_score:
        min_score = scores[i]
        amazing_count += 1

print(amazing_count)