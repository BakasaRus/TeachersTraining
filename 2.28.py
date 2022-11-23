x = 4 ** 2014 + 2 ** 2015 - 8
b = bin(x)[2:]
print(b.count('1'))
print(b.count('0'))
print(b)
