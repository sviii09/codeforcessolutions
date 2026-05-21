a, b = map(int, input().split())

different_days = min(a, b)
same_days = (max(a, b) - different_days) // 2

print(different_days, same_days)