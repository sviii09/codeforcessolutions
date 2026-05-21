t = int(input())
codeforces = set("codeforces")

for _ in range(t):
    c = input().strip()
    if c in codeforces:
        print("YES")
    else:
        print("NO")