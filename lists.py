numbers = [8, 5, 10, 47, 7, 55, 10]
mixed = [0, 7.5, "Test"]

print(numbers)
print(numbers[1])
print(mixed[2])
print(numbers[-1])
# print(numbers[10])

print(numbers[2:4])
print(numbers[:4])
print(numbers[2:])
print(numbers[:])
print(numbers[2:7:2])
print(numbers[-3:-1])
print(numbers[::-1])

print(numbers + mixed)
print(mixed * 2)

print(len(numbers))

for i in range(len(numbers)):
    numbers[i] += 1

for x in numbers:
    print(x)

print(min(numbers))
print(max(numbers))

print(numbers.count(11))
print(0 in numbers)
print(numbers.index(56))

print(numbers)

numbers.append(0)
print(numbers)

numbers.insert(3, 20)
print(numbers)

numbers.sort()
print(numbers)

numbers.pop()
print(numbers)

numbers.pop(1)
print(numbers)
