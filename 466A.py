n, m, a, b = map(int, input().split())

# Calculate cost for each strategy
single_only = n * a
multi_only = ((n + m - 1) // m) * b  # ceil division

# Mixed strategy: buy (n // m) multi-ride tickets and single tickets for the remainder
remainder = n % m
mixed = (n // m) * b + remainder * a

# Special case: sometimes it's cheaper to buy an extra multi-ride ticket 
# than to buy single tickets for the remainder
extra_multi = ((n + m - 1) // m) * b  # same as multi_only
mixed_extra = (n // m) * b + b  # buy one more multi-ride ticket

# Take the minimum of all possible strategies
result = min(single_only, multi_only, mixed, mixed_extra)

print(result)