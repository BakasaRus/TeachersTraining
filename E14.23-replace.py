file = open('E14/24.4.txt', 'r')
data = file.readline()
file.close()

data = data.replace('O', 'A') \
           .replace('D', 'C') \
           .replace('F', 'C') \
           .replace('CA', '-') \
           .replace('A', ' ') \
           .replace('C', ' ')

print(max(len(part) for part in data.split()))
