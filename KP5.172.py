total = 0
maximum = 0

for x in range(10000 + 1):
    if x % 16 == 9 and x % 25 == 6:
        total += x
        maximum = x

print(maximum, total)
