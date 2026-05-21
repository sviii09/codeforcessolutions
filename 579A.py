x = int(input())

# Count the number of 1's in binary representation
# bin(x) returns a string like '0b101', count the '1's in it
answer = bin(x).count('1')

print(answer)