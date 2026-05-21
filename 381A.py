n = int(input())
cards = list(map(int, input().split()))

sereja_score = 0
dima_score = 0

left = 0
right = n - 1

for turn in range(n):
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1
    
    if turn % 2 == 0:
        sereja_score += chosen
    else:
        dima_score += chosen

print(sereja_score, dima_score)