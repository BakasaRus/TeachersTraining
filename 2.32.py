def to_base(x, base):
    res = ''
    while x > 0:
        res = str(x % base) + res
        x //= base
    return res


x = 27 ** 11 + 3 ** 19 - 9 ** 7 - 9
res = to_base(x, 3)
print(res)
print(res.count('2'))
