n = int(input())
s = input().lower()

letters = set(s)

if len(letters) == 26:
    print("YES")
else:
    print("NO")