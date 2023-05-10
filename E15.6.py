file = open('E15/26.6.txt', 'r')
n = int(file.readline())
# Здесь именно множество, а не список, даёт существенный прирост
# в скорости за счёт быстрой проверки на наличие числа
numbers = {int(line) for line in file}
file.close()

even = [x for x in numbers if x % 2 == 0]

count = 0
result = 10 ** 9 + 1

for i in range(len(even) - 1):
    for j in range(i + 1, len(even)):
        if (even[i] + even[j]) // 2 in numbers:
            count += 1
            result = min(result, (even[i] + even[j]) // 2)

print(count, result)
