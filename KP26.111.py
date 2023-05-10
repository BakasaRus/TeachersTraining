file = open('26-111.txt', 'r')

k = int(file.readline())
n = int(file.readline())

requests = []
for i in range(n):
    start, end = [int(x) for x in file.readline().split()]
    requests.append([start, end])

file.close()

requests.sort()

is_empty = [-1] * k

count = 0
last_place = 0
for request in requests:
    start, end = request
    for i in range(k):
        if is_empty[i] < start:
            is_empty[i] = end
            count += 1
            last_place = i + 1
            break

print(count, last_place)
