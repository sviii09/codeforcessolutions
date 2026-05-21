n = int(input())
groups = list(map(int, input().split()))

count = [0, 0, 0, 0]  # count of groups with size 1, 2, 3, 4

for s in groups:
    count[s-1] += 1

# Each group of 4 needs its own taxi
taxis = count[3]  # groups of size 4

# Groups of 3 can pair with groups of 1
taxis += count[2]  # each group of 3 needs a taxi
count[0] = max(0, count[0] - count[2])  # use as many 1's as possible with 3's

# Groups of 2 can pair with each other or with 1's
taxis += count[1] // 2  # pairs of 2's
count[1] = count[1] % 2  # remaining group of 2 (0 or 1)

# If there's a remaining group of 2, it needs a taxi and can take up to 2 groups of 1
if count[1] == 1:
    taxis += 1
    count[0] = max(0, count[0] - 2)  # use up to 2 ones with the remaining 2

# Remaining groups of 1 need their own taxis (4 per taxi)
taxis += (count[0] + 3) // 4  # ceiling division

print(taxis)