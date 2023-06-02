def let4(n: int) -> int:
    n = bin(n)[2:]
    n = f'{n}{n[1]}{n[-2]}'
    return int(n, 2)


for i in range(5, 1000):
    if let4(i) > 180: print(i)