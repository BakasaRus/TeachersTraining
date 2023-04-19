count = 0
minimum = 0

for x in range(9999, 1111-1, -1):
    delims = 0
    for i in 5, 11, 17, 19:
        if x % i == 0:
            delims += 1
    if delims == 2:
        count += 1
        minimum = x

print(count, minimum)
