def f(i, x):
    # ИЛИ(И(B2=A$19; D2=B$19); И(C2=C$19; E2=D$19); И(C2=E$19; D2=F$19))
    i = f'{i:04b}'
    x = f'{x:06b}'
    first = i[0] == x[0] and i[2] == x[1]
    second = i[1] == x[2] and i[3] == x[3]
    third = i[1] == x[4] and i[2] == x[5]
    return first or second or third


for x in range(0b111111 + 1):
    diagram = [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1]
    ok = all(f(i, x) == bool(diagram[i]) for i in range(16))
    if ok:
        print(f'{x:06b}')
