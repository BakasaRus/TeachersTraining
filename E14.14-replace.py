file = open('E14/24.1.txt', 'r')  # r -- режим открытия файла, подробнее в материалах
data = file.readline()
file.close()

# XZYXZYX посчитает неправильно
# print(data.count('XZYX'))

while 'XZYXZYX' in data:
    data = data.replace('XZYXZYX', 'XZYXXZYX')

print(data.count('XZYX'))
