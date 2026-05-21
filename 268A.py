n = int(input())

home_colors = []
guest_colors = []

for _ in range(n):
    h, a = map(int, input().split())
    home_colors.append(h)
    guest_colors.append(a)

count = 0
for i in range(n):
    for j in range(n):
        if i != j and home_colors[i] == guest_colors[j]:
            count += 1

print(count)