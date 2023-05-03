file = open('E15/26.1.txt', 'r')
free_space, files_count = [int(x) for x in file.readline().split()]
files = [int(line) for line in file]  # Продолжаем читать файл со второй строчки
file.close()

files.sort()

count = 0
max_file = 0

for x in files:
    if free_space - x >= 0:
        free_space -= x
        count += 1
        max_file = x
    elif free_space + max_file - x >= 0:
        free_space = free_space + max_file - x
        max_file = x
    else:
        break

print(count, max_file)
