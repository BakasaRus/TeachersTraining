x = int(input())
base = 3
while x > 0:
    print(x % base)
    # x = x // base
    x //= base

# range(5) -> 0 1 2 3 4
# range(5, 10) -> 5 6 7 8 9
# range(10, 20, 2) -> 10 12 14 16 18
# range(10, 5) -> :(
# range(10, 5, -1) -> 10 9 8 7 6

for i in range(20):
    if i == 15:
        continue
    print(i)

while True:
    # ...
    if x == 0:
        break

