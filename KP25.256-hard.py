for a in 2, 4, 6, 8, 0:
    for b in 1, 3, 5, 7, 9:
        for c in range(10):
            x = int(f'12{a}4{b}6{c}8')
            if x % 92 == 0:
                print(x, x // 92)
