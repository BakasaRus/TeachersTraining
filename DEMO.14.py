for x in '0123456789ABCDE':
    a = int('123' + x + '5', 15)
    b = int('1' + x + '233', 15)
    if (a + b) % 14 == 0:
        print(x, (a + b) // 14)
