import math

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    cnt1 = s.count('1')
    
    if cnt1 == 0:

        print((n + 1) // 2)
        continue
    
    
    zeros = []
    i = 0
    while i < n:
        if s[i] == '0':
            j = i
            while j < n and s[j] == '0':
                j += 1
            zeros.append((i, j - 1))  
            i = j
        else:
            i += 1
    
    total_new = 0
    for start, end in zeros:
        L = end - start + 1
        if start == 0 or end == n - 1:
            
            total_new += (L + 1) // 3  
            
        else:
            
            total_new += (L + 1) // 3  
            
    
total_new = 0
for start, end in zeros:
    L = end - start + 1
    if start == 0 or end == n - 1:
        total_new += (L + 1) // 3
    else:
        total_new += L // 3

print(cnt1 + total_new)