n = int(input())
percentages = list(map(int, input().split()))

total_sum = sum(percentages)
result = total_sum / n

print(result)