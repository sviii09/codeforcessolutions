word = input().strip()

upper_count = sum(1 for ch in word if ch.isupper())
lower_count = len(word) - upper_count

if upper_count > lower_count:
    print(word.upper())
else:
    print(word.lower())