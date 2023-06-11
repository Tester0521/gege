# 28120


def kill_imposters(arr: list) -> list:
    imposters = []
    for el in arr:
        c = 0
        for el2 in arr:
            if el % el2 == 0: c += 1
        if c > 1:
            imposters.append(el)
    arr = list(filter(lambda x: x not in imposters, arr))
    return arr



def _1() -> print:
    arr = [i for i in range(201455, 201471)]
    divs = [i for i in range(2, int(201470**0.5) + 1)] # kill_imposters([i for i in range(2, int(201470**0.5) + 1)])
    print(divs)
    for el in arr:
        test = []
        for el2 in divs:
            if len(test) > 2: break
            elif el % el2 == 0:
                test.append(el2)
                test.append(el // el2)
        if len(test) == 2:
            test.append(el)
            test.append(1)
            print(sorted(test))


# 33527

def def2() -> print:
    divs, gg = kill_imposters([i for i in range(2, int(102_000_000**0.5)+ 1, 2)]), [x for x in range(101_000_000, 102_000_001, 2) if int(x**0.5) * int(x**0.5) == x]
    for x in gg:
        for y in divs:
                if (x % y == 0) and (y not in [2, int(x**0.5), x]): break
        print(x)



# def2()


# 36880

def krabik():
    M, N = [i for i in range(2, 30, 2)], [i for i in range(1, 30, 2)]
    for m in M:
        for n in N:
            x = 2**m * 3**n
            if 400_000_000 <= x <= 600_000_000:
                print(x)
# krabik()


# 33527
def lobster() -> print:
    divs = [i for i in range(2, int(102_000_000**0.5) + 1, 2) if all(i % x != 0 for x in range(2, i))]

    for x in range(101_000_000, 102_000_001, 2):
        if x**0.5 % 2 == 0:
            print(x)

# lobster()


# 27852

def pingui():
    divs = [i for i in range(2, int(185_330**0.5) + 1) if all(i % y != 0 for y in range(2, i))]
    print(divs)
    for x in range(185_311, 185_330):
        res = [1, x]
        for y in divs:
            if len(res) > 4: break
            elif x % y == 0:
                res.append(y)
                res.append(x // y)
        if len(res) == 4:
            print(sorted(res))

# pingui()

def wtf() -> print:
    res = []
    for x in range(600_001, 1_000_000):
        if len(res) == 5: break
        c = 0
        for y in range(17, 7777, 10):
            if c > 1: break
            elif x % y == 0:
                res.append((x, y))
                c += 1
    print(res)
# wtf()

# 46983

def M(n: int) -> int:
    d = [i for i in range(2, int(n**0.5) + 1) if n % i == 0]
    if len(d) > 5: return n // d[4]
    else: return 0

def antilopa():
    for N in range(460_000_000, 461_000_000):
        if M(N) > 0:
            print(M(N))

# antilopa()


# 47022
def gazel():
    rs = []
    def M(n: int) -> int:
        d = [i for i in range(int(n**0.5) + 1, 1, -1) if n % i == 0]
        if len(d) >= 5: return n // d[4]
        else: return 0

    for N in range(300_000_000, 300_010_000):
        if M(N) > 0:
            rs.append(M(N))
        if len(rs) == 5: return rs

# print(gazel())

from fnmatch import *
print([[x, x // 2023] for x in range(2023, 10**10, 2023) if fnmatch(str(x), '1?2139*4')])
