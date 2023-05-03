file = open('E14/24.4.txt', 'r')
data = file.readline()
file.close()

count = 0
max_count = 0
i = 0

while i < len(data) - 1:
    if data[i] in 'CDF' and data[i+1] in 'AO':
        count += 1
        i += 2
    else:
        max_count = max(max_count, count)
        count = 0
        i += 1

print(max_count)
