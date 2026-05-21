n, m = map(int, input().split())

for i in range(1, n + 1):
    # If current row is odd, fill entire row with '#'
    if i % 2 == 1:
        print('#' * m)
    else:
        # For even rows, alternate pattern
        # For rows 2, 6, 10, ... (i % 4 == 2) - snake goes right, so '#' at the end
        if i % 4 == 2:
            print('.' * (m - 1) + '#')
        # For rows 4, 8, 12, ... (i % 4 == 0) - snake goes left, so '#' at the beginning
        else:
            print('#' + '.' * (m - 1))