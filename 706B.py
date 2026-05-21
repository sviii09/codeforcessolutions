n = int(input())
prices = list(map(int, input().split()))
q = int(input())

prices.sort()

for _ in range(q):
    m = int(input())
    
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if prices[mid] <= m:
            left = mid + 1
        else:
            right = mid
    
    print(left)