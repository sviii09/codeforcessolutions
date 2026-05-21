import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    idx = 1
    results = []
    INF = 10**9
    for _ in range(t):
        A = [int(c) for c in input_data[idx]]
        idx += 1
        B = [int(c) for c in input_data[idx]]
        idx += 1
        n = len(A)
        dp0, dp1 = 0, INF
        for i in range(n):
            new_dp0 = min(
                dp0 + (0 != B[i]) + ((0 ^ 0) != A[i]),
                dp1 + (0 != B[i]) + ((0 ^ 1) != A[i])
            )
            new_dp1 = min(
                dp0 + (1 != B[i]) + ((1 ^ 0) != A[i]),
                dp1 + (1 != B[i]) + ((1 ^ 1) != A[i])
            )
            dp0, dp1 = new_dp0, new_dp1
        results.append(str(min(dp0, dp1)))
    print("\n".join(results))

if __name__ == "__main__":
    solve()