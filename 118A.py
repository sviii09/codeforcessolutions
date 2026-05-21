s = input().strip()

vowels = set("aoyeuiAOYEUI")

result = []
for ch in s:
    if ch in vowels:
        continue
    else:
        result.append('.' + ch.lower())

print(''.join(result))