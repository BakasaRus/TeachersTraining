for A in range(1000000):
    ok = True
    for x in range(1000000):
        F = ((x & 19 == 0) <= (x & 56 != 0)) <= (x & A != 0)
        if not F:
            ok = False
            break
    if ok:
        print(A)
        break
