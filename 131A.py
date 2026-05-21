word = input().strip()

# Check if the word needs correction
# Condition: either all letters are uppercase, or all except first are uppercase
if word.isupper() or (len(word) > 1 and word[1:].isupper() and word[0].islower()):
    # Swap case of all letters
    result = word.swapcase()
else:
    result = word

print(result)