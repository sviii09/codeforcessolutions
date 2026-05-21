t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_len = 0
    curr_len = 0
    
    for x in arr:
        if x == 0:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0
    
    print(max_len)