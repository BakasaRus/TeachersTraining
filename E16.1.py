file = open('E16/27.1-A.txt')

n = int(file.readline())
k = 6
data = [int(line) for line in file]

file.close()

min_before_window = 10000
min_prod = 10000 ** 2

for i in range(k, n):
    min_before_window = min(min_before_window, data[i - 6])
    min_prod = min(min_prod, min_before_window * data[i])

print(min_prod)
