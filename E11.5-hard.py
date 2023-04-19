from tqdm import tqdm

a, b = 174_457_00, 174_505_00

sieve = [x for x in range(b + 1)]
sieve[1] = 0
primes = []
for x in tqdm(sieve):
    if x == 0:
        continue
    primes.append(x)
    for i in range(2 * x, b + 1, x):
        sieve[i] = 0

primes = set(primes)

for x in tqdm(range(a, b + 1)):
    for i in primes:
        if x % i == 0 and x // i in primes:
            # print(i, x // i)
            break
