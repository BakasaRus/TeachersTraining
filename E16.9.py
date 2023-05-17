file = open('E16/27.9-B.txt', 'r')

n = int(file.readline())
max_sum = 0
min_diff = 100000

for line in file:
    a, b = [int(x) for x in line.split()]
    max_sum += max(a, b)
    cur_diff = abs(a - b)
    if cur_diff % 3 != 0:
        min_diff = min(min_diff, cur_diff)

file.close()

if max_sum % 3 != 0:
    print(max_sum)
else:
    print(max_sum - min_diff)
