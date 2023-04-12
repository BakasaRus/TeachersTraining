string = 'ABCD'
for i in range(4):
    string *= 2
    pos_1 = len(string) // 4
    pos_2 = 3 * pos_1
    string = string[:pos_1] + string[pos_2:] + string[pos_1:pos_2]
    print(string)

for i in 60, 37, 44, 51:
    print(string[i - 1])
