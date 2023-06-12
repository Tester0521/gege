from itertools import *



def base(n: int, toBase: int) -> int:
    res, al = '', '0123456789abcdefg'
    while n > 0:
        n, m = divmod(n, toBase)
        res += al[m]
    return res[::-1]

def prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True

def _25_():
    for x in range(101_000_000, 102_000_001, 2):
        if ( (x // 2) ** 0.5 == int((x//2) ** 0.5) ) and (prime((x//2) ** 0.5)): print(x)

from fnmatch import *
def __25__():
    res = [[x, x // 2023] for x in range(2023, 10**10, 2023) if fnmatch(str(x), '1?2139*4')]
    return res

def _2_():
    # False zwyx
    # f = lambda x, y, z, w: ((w <= (y == z)) and (y == (z <= x)))
    # ultra = [[[x1, 0, 0, 0, True], [0, x2, 1, 1, True], [0, 0, 0, 1, False]] for x1, x2 in product([0, 1], repeat = 2)]
    # f = lambda x, y, z, w: ((not(z == w)) <= (w and not(x))) or (x and not(y))
    # ultra = [[[0, x1, 0, 0, False], [0, x2, x3, 0, False], [0, x4, x5, x6, False]] for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat = 6)]
    f = lambda x, y, z, w: ((y <= w) == (x <= (not z))) and (x or w)
    ultra = [[[0, 1, 1, 1, False], [1, 0, 1, 0, True], [x1, 0, 0, x2, True]] for x1, x2 in product([0,1], repeat = 2)]
    for el in ultra:
        res = [(x, y, z, w) for x, y, z, w in permutations(range(4)) if all(f(row[x], row[y], row[z], row[w]) == row[-1] for row in el)]
        if len(res) == 1: print(el, res)
_2_()

def _22_(f = open('./src/lab/22csv.csv')):
    arr = [el.split(',') for el in f][1:]
    d = {}
    for el in arr:
        key, time, dep = el[0], int(el[1]), el[-1].replace('\n', '')
        dep = dep.split(';')
        if dep[0] == '': d[key] = time
        else: d[key] = max([d[x] for x in dep]) + time + 3
    print(max(d.values()))

def _27_A(f = open('./src/lab/27-A-2.txt')):
    arr = sorted([int(el) for el in f][1:])
    lol = [el % 3 for el in arr]
    print(lol)

    return sum([arr[-2], arr[-3], arr[-5]])

def _27(f = open('./src/lab/27-B-2.txt')):
    # arr = [[int(el), int(el) % 3]  for el in f][1:]
    # arr.sort(key = lambda x: x[0])
    arr = sorted([int(el) for el in f][1:])[::-1]
    lol = [el % 3 for el in arr]
    print(lol)

    # arr.remove(arr[0])
    # arr.remove(arr[2])
    # arr.remove(arr[3])
    return arr[0] + arr[2] + arr[5]
