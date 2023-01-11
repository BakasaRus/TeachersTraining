# range(5) -> 0 1 2 3 4
# range(5, 8) -> 5 6 7
# range(8, 16, 2) -> 8 10 12 14
# range(16, 8, -2) -> 16 14 12 10
for x in range(1000000, 0, -1):
    if (90 < x * x) <= (x < x - 1):
        print(x)
        break
