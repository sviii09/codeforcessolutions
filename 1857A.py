t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    total_sum = sum(arr)
    
    # If total sum is odd, impossible
    if total_sum % 2 == 1:
        print("NO")
        continue
    
    # Count odd numbers
    odd_count = sum(1 for x in arr if x % 2 == 1)
    
    # If there's at least one odd number, odd_count must be even
    # and we need at least one in each group (n ≥ 2 ensures this if odd_count ≥ 2)
    if odd_count % 2 == 0:
        print("YES")
    else:
        print("NO")