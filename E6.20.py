from math import floor, ceil

res_A = 0
res_B = 0
length = 0
for a in range(0, 600):
    for b in range(a + 1, 600):
        ok = True
        A = a / 10
        B = b / 10
        for x in range(-100, 100):
            F = ((11 <= x < 36) <= (not (21 < x <= 55))) <= (not (A <= x <= B))
            if not F:
                ok = False
                break
        if ok and B - A > length:
            res_A = A
            res_B = B
            length = B - A

print(floor(res_A), ceil(res_B), ceil(res_B) - floor(res_A))
