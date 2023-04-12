word = 'ЭЛЕКТРОН'
result = word

for i in range(500):
    word = word[1:] + word[0]
    result = word + result
    print(500 - i, word)

print(result)
print(result[2987 - 1])
