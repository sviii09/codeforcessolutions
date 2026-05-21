t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Check first three elements to determine the common value
    if arr[0] == arr[1]:
        common = arr[0]
    elif arr[0] == arr[2]:
        common = arr[0]
    else:
        common = arr[1]
    
    # Find the index of the element that's different
    for i in range(n):
        if arr[i] != common:
            print(i + 1)  # +1 because indexing is 1-based
            break