file = open('E15/26.7.txt', 'r')

n = int(file.readline())
boxes = [int(line) for line in file]

file.close()

boxes.sort(reverse=True)

count = 0
current_box = 10_005

for box in boxes:
    if current_box - box >= 3:
        current_box = box
        count += 1

print(count, current_box)
