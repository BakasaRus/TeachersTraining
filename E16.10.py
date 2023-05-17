file = open('E16/27.10-B.txt', 'r')

n = int(file.readline())
data = []

for line in file:
    a, b = [int(x) for x in line.split()]
    if b % 36 == 0:
        b //= 36
    else:
        b = b // 36 + 1
    data.append([a, b])

file.close()

current_sum = 0
left = 0
right = 0
min_sum = 10 ** 100

for i in range(1, n):
    current_sum += data[i][1] * (data[i][0] - data[0][0])
    right += data[i][1]

for i in range(1, n):
    left += data[i - 1][1]
    current_sum = current_sum + (data[i][0] - data[i - 1][0]) * left - (data[i][0] - data[i - 1][0]) * right
    right -= data[i][1]
    min_sum = min(min_sum, current_sum)

print(min_sum)
