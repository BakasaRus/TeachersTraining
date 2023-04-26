from re import match

for i in range(0, 10 ** 7 + 1):
    if match('^9.+55.*7$', str(i)):
        print(i)
