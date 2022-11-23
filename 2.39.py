def R(N):
    b = bin(N)[2:]
    for i in range(2):
        if b.count('1') % 2 == 1:
            b += '1'
        else:
            b += '0'
    return int(b, 2)


# 11010 -> 1101010 = 64 + 32 + 8 + 2 = 106
for N in range(1, 10000):
    if R(N) > 105:
        print(N)
        break
