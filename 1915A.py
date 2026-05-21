t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    # Compare each digit with the others to find the unique one
    if a == b:
        print(c)
    elif a == c:
        print(b)
    else:  # b == c
        print(a)