t = int(input())

for _ in range(t):
    n = input().strip()
    length = len(n)
    
    round_numbers = []
    
    for i in range(length):
        digit = int(n[i])
        if digit != 0:
            round_numbers.append(digit * (10 ** (length - i - 1)))
    
    print(len(round_numbers))
    print(' '.join(map(str, round_numbers)))