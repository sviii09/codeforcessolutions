s = input()
target = "hello"
pos = 0  # position in target

for ch in s:
    if ch == target[pos]:
        pos += 1
        if pos == len(target):
            break

print("YES" if pos == len(target) else "NO")