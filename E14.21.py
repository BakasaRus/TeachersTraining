file = open('E14/24.3.txt', 'r')
lines = file.readlines()
file.close()

selected_line = ''
selected_count = 0

for line in lines:
    if line.strip().count('A') > selected_count:
        selected_line = line.strip()
        selected_count = line.count('A')

print(selected_line)

letters_count = {}

for i in range(1, len(selected_line) - 1):
    if selected_line[i-1] != selected_line[i+1]:
        continue
    if selected_line[i] in letters_count:
        letters_count[selected_line[i]] += 1
    else:
        letters_count[selected_line[i]] = 1

print(letters_count)

max_letter = max(letters_count)

for letter in letters_count:
    if letters_count[letter] > letters_count[max_letter]:
        max_letter = letter

print(max_letter)
