n = int(input())
arr = list(map(int, input().split()))

# If there's only one element, the longest non-decreasing subsegment is 1
if n == 1:
    print(1)
else:
    max_length = 1  # At minimum, a single element forms a non-decreasing subsegment
    current_length = 1
    
    for i in range(1, n):
        # If current element is >= previous element, extend the current subsegment
        if arr[i] >= arr[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            # Start a new subsegment
            current_length = 1
    
    print(max_length)