import math

def solve():
    t = int(input())
    for _ in range(t):
        l, a, b = map(int, input().split())
        g = math.gcd(b, l)
        r = a % g
        ans = l - g + r
        print(ans)

if __name__ == "__main__":
    solve()