from re import match

for i in range(0, 10 ** 10 + 1, 2023):
    if match('^1.2139.*4$', str(i)):
        print(i, i // 2023)
