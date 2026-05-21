n = input().strip()

# Step 1: Count lucky digits in n
lucky_digit_count = sum(1 for ch in n if ch in '47')

# Step 2: Check if lucky_digit_count itself is lucky
count_str = str(lucky_digit_count)
is_lucky = all(ch in '47' for ch in count_str) and lucky_digit_count > 0

print("YES" if is_lucky else "NO")