n, k, l, c, d, p, nl, np = map(int, input().split())

total_drink = k * l
total_limes = c * d

toasts_by_drink = total_drink // nl
toasts_by_lime = total_limes
toasts_by_salt = p // np

total_toasts = min(toasts_by_drink, toasts_by_lime, toasts_by_salt)

print(total_toasts // n)