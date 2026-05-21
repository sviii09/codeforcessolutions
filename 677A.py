n, h = map(int, input().split())
heights = list(map(int, input().split()))

tall = sum(1 for height in heights if height > h)
width = n + tall

print(width)