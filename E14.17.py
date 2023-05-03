file = open('E14/24.3.txt', 'r')
lines = file.readlines()
file.close()

count = 0
for line in lines:
    if line.count('A') > line.count('Z'):
        count += 1

print(count)
