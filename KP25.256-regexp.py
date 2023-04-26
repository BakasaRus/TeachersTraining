from re import match

for i in range(0, 10 ** 8 + 1, 92):
    if match('^12[24680]4[13579]6.8$', str(i)):
        print(i, i // 92)
