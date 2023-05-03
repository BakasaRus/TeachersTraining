file = open('E14/24.1.txt', 'r')  # r -- режим открытия файла, подробнее в материалах
data = file.readline()
file.close()

# XYZXXYZXYZXYZ
count = 1
max_count = 0

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 1

print(max_count)
