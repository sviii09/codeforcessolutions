s = input().strip()

# Extract digits (ignore '+')
digits = [ch for ch in s if ch.isdigit()]

# Sort digits
digits.sort()

# Join with '+'
result = '+'.join(digits)

print(result)