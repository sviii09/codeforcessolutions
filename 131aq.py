word = input().strip()

# Check if the word needs correction
if word.isupper() or (len(word) > 1 and word[0].islower() and word[1:].isupper()):
    # Swap case of all letters
    result = word.swapcase()
else:
    result = word

print(result)