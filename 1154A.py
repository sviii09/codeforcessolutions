numbers = list(map(int, input().split()))
numbers.sort()

a_plus_b = numbers[0]
a_plus_c = numbers[1]
b_plus_c = numbers[2]
total = numbers[3]

a = total - b_plus_c
b = total - a_plus_c
c = total - a_plus_b

print(a, b, c)