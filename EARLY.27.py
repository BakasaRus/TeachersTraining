file = open('E16/27.EARLY-B.txt')

k = int(file.readline())
n = int(file.readline())
data = [int(line) for line in file]

file.close()

max_before_window = 0
max_sum = 0

for i in range(k, n):
    max_before_window = max(max_before_window, data[i - k])
    max_sum = max(max_sum, max_before_window + data[i])

print(max_sum)
