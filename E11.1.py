from tqdm import tqdm

count = 0
maximum = 0
for x in tqdm(range(1016000 + 1, 7937000 + 1, 3)):
    if x % 7 != 0 and x % 17 != 0 and x % 19 != 0 and x % 27 != 0:
        count += 1
        maximum = x

print(count, maximum)
