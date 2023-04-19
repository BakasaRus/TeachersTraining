def f(x):
    return x ** 2 + 8


number = int(input())

if number > 0:
    print('Positive')
elif number == 0:
    print('Zero')
else:
    print('Negative')

numbers = [int(x) for x in input().split()]
for x in numbers:
    print(f(x))
