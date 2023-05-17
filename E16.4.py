file = open('E16/27.4-B.txt', 'r')

n = int(file.readline())
k = 93

current_sum = 0
mins = [0] * k
diffs = [0] * k

for line in file:
    x = int(line)
    current_sum += x
    if mins[current_sum % k] == 0:
        mins[current_sum % k] = current_sum
    else:
        diff = current_sum - mins[current_sum % k]
        if diff % 2 == 1:
            diffs[current_sum % k] = current_sum - mins[current_sum % k]

file.close()

diffs[0] += mins[0]

print(max(diffs))
