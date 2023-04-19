for i in range(0, 10 ** 10 + 1, 2023):
    x = str(i)
    if x[-1] == '4' and x[0] == '1' and x[2:6] == '2139':
        print(i, i // 2023)
