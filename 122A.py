n = int(input())
lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

almost_lucky = False
for lucky in lucky_numbers:
    if n % lucky == 0:
        almost_lucky = True
        break

print("YES" if almost_lucky else "NO")