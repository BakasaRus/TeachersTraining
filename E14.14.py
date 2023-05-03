file = open('E14/24.1.txt', 'r')  # r -- режим открытия файла, подробнее в материалах
data = file.readline()
file.close()

# XZYXZYX посчитает неправильно
# print(data.count('XZYX'))

count = 0

for i in range(len(data) - 3):
    if data[i:i + 4] == 'XZYX':
        count += 1

print(count)
