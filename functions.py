import math


def factorial(x=1):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
    print('Hello!')


# C(n, k) = n! / k! / (n-k)!

n, k = 7, 3
print(factorial())
print(factorial(5))
C = factorial(n) // factorial(k) // factorial(n - k)
print(C)
