def R(N):
    b = bin(N)[2:]
    if b.count('1') % 2 == 0:
        b += '0'
        b = '10' + b[2:]
    else:
        b += '1'
        b = '11' + b[2:]
    return int(b, 2)


for N in range(1, 10000):
    if R(N) > 40:
        print(N)
        break
