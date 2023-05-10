file = open('E15/26.2.txt', 'r')
n = int(file.readline())
places = {}

# В 5-ом ряду заняты места 3 и 8, в 17-ом - 15 и 24
# {
#   5: [3, 8],
#   17: [15, 24]
# }

for i in range(n):
    row, place = [int(x) for x in file.readline().split()]
    if row in places:
        places[row].append(place)
    else:
        places[row] = [place]

file.close()

# 3: | | |x|x| | |x| |

max_row = 0
selected_place = 0

for row in places:
    places[row].sort()
    for i in range(len(places[row]) - 1):
        if places[row][i+1] - places[row][i] == 3 and row > max_row:
            max_row = row
            selected_place = places[row][i] + 1
            break

print(max_row, selected_place)
