def to_base(x, base):
    res = ''
    while x > 0:
        res = str(x % base) + res
        x //= base
    return res


x = 27 ** 8 + 3 ** 25 - 81
res = to_base(x, 3)
for i in '012':
    print(i, res.count(i))
