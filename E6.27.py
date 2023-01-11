for A in range(1, 1000000):
    ok = True
    for x in range(1, 1000000):
        F = (x % A == 0) <= (x % 14 != 0 or x % 21 == 0)
        if not F:
            ok = False
            break
    if ok:
        print(A)
        break
