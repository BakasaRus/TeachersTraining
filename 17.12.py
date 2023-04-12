def K(x, end):
    if x == end:
        return 1
    if x > end:
        return 0

    return K(x + 1, end) + K(x * 2, end)


result = K(2, 22)
print(result)
