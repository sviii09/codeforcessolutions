n, m, a = map(int, input().split())

# Ceil division for rows and columns
rows = (n + a - 1) // a
cols = (m + a - 1) // a

print(rows * cols)