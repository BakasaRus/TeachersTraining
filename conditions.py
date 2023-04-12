# 13 8 10
# "13 8 10" -> ['13', '8', '10'] -> [13, 8, 10]
a, b, c = [int(x) for x in input().split()]

result = a > b
print(result)
result = (b == c)
print(result)
result = (a != c)
print(result)

result = a > b and a > c
print(result)
result = not (b < a or b > 0)
print(result)
result = b < c < a  # b < c and c < a
print(result)

if a > b and a > c:
    print('Maximum:', a)
elif b > c:
    print('Maximum:', b)
else:
    print('Maximum:', c)

x = a + b + c
y = 7 * x if x < 0 else 5 * x + 2
# if x < 0:
#     y = 7 * x
# else:
#     y = 5 * x + 2
print(y)

if a > b:
    if a > c:
        print(a)
