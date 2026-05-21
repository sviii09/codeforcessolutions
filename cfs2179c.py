import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx:idx+n])); idx += n
        m = min(arr)
        # find smallest positive difference with m
        min_diff = 10**18
        for v in arr:
            if v > m:
                min_diff = min(min_diff, v - m)
        if min_diff == 10**18:  # all equal? but problem says distinct, so not possible unless n=1, but n≥2
            min_diff = 0
        if min_diff >= m + 1:
            out.append(str(min_diff))
        else:
            out.append(str(m))
    print("\n".join(out))

if __name__ == "__main__":
    solve()