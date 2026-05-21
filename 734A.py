n = int(input())
s = input().strip()

anton_wins = s.count('A')
danik_wins = n - anton_wins

if anton_wins > danik_wins:
    print("Anton")
elif anton_wins < danik_wins:
    print("Danik")
else:
    print("Friendship")