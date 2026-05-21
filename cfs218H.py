def divisors(x):
    divs = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            divs.append(i)
            if i != x // i:
                divs.append(x // i)
        i += 1
    return divs

def solve():
    w, h, d = map(int, input().split())
    n = int(input())

    div_w = divisors(w)
    div_h = divisors(h)

    for a in div_w:
        for b in div_h:
            if n % (a * b) == 0:
                c = n // (a * b)
                if c > 0 and d % c == 0:
                    print(a - 1, b - 1, c - 1)
                    return
    print(-1)

if __name__ == "__main__":
    solve()