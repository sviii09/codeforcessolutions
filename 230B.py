import math

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

# Precompute primes up to 10^6
MAX = 10**6
is_prime = sieve(MAX)

n = int(input())
numbers = list(map(int, input().split()))

for x in numbers:
    r = int(math.isqrt(x))
    if r * r == x and is_prime[r]:
        print("YES")
    else:
        print("NO")