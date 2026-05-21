# Read the three coordinates
x1, x2, x3 = map(int, input().split())

# Find min and max
min_coord = min(x1, x2, x3)
max_coord = max(x1, x2, x3)

# The answer is the range
answer = max_coord - min_coord

# Output the result
print(answer)