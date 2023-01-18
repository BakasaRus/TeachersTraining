for A in range(1, 10000):
    for x in range(1, 10000):
        F = ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80)
        if not F:
            break
    else:
        print(A)
        break
