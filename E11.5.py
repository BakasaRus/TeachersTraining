from tqdm import tqdm

for x in tqdm(range(174_457_00, 174_505_00 + 1)):
    delims = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            delims.add(i)
            delims.add(x // i)
    if len(delims) == 2:
        pass
        # print(delims[0], delims[1])
