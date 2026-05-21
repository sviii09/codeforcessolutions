t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    # Put the three numbers in a list and sort them
    numbers = [a, b, c]
    numbers.sort()
    
    # The middle element (index 1) is the medium number
    print(numbers[1])