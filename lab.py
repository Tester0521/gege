from itertools import *


# 2 371137
#
# f = lambda a, b, c, d: (((not(a)) and (not(b))) or (b == c) or d)
# arr = [[[x1, x2, 1, x3], [1, 0, x4, 1], [0, 0, 1, 1]] for x1, x2, x3, x4 in product([0, 1], repeat = 4)]
# for el in arr:
#     res = [(a, b, c, d) for a, b, c, d in permutations(range(4)) if all(f(row[a], row[b], row[c], row[d]) == False for row in el)]
#     print(res)


# 5 33084
#
# def f(n: int):
#     s = ''
#     arr = [int(x) for x in bin(n)[2:]]
#     sumx = sum(arr)
#     arr.append(sumx % 2)
#     sumx = sum(arr)
#     arr.append(sumx % 2)
#     for el in arr:
#         s += str(el)
#     return int(s, 2)
# for i in range(1, 10000):
#     if f(i) > 154:
#         print(i)
#         break

#  8 8658
#
# arr = [list(x) for x in product(['А', 'Н', 'П'], repeat = 5)]
# print(arr[200])

# 12 33482

# def gg(i: int):
#     s = '1' * i
#     while '111' in s:
#         s = s.replace('111', '22', 1)
#         s = s.replace('222', '11', 1)
#     return s.count('1')
#
# res = []
# for i in range(101, 999):
#     res.append([i, gg(i)])
# res.sort(key = lambda x: x[1])
# print(res)



# 14 15111
#
# x = 25**5 + 5**14 - 5
#
# def base(n: int):
#     res, al = '', '0123456789'
#     while n > 0:
#         n, m = divmod(n, 5)
#         res += al[m]
#     return res[::-1]
# print(base(x).count('4'))


# 15 18797
# f = lambda A, x, y: (x > A) or (y > x) or ((y * 2 + x) < 110)
#
# for A in range(1000):
#     for x, y in product(range(1000), repeat = 2):
#             if not(f(A, x, y)): break
#     else: print(A)

# 19-21 28083-28085
def rock(x, t):
    if x >= 26 and t == 3: return 1
    elif x < 26 and t == 3: return 0
    elif x >= 26 and t < 3: return 0
    else: return rock(x + 1, t + 1) or rock(x * 2, t + 1)

# for i in range(1, 26):
#     if rock(i, 1): print(i)

# def rock2(x, t):
#     if x >= 26 and t == 4: return 1
#     elif x < 26 and t == 4: return 0
#     elif x >= 26 and t < 4: return 0
#     else:
#         if t % 2 != 0: return rock2(x + 1, t + 1) or rock2(x * 2, t + 1)
#         else: return rock2(x + 1, t + 1) and rock2(x * 2, t + 1)
#
# for i in range(1, 26):
#     if rock2(i, 1): print(i)

# def rock3(x, t):
#     if x >= 26 and (t == 3 or t == 5): return 1
#     elif x < 26 and t == 5: return 0
#     elif x >= 26 and t < 5: return 0
#     else:
#         if t % 2 == 0: return rock3(x + 1, t + 1) or rock3(x * 2, t + 1)
#         else: return rock3(x + 1, t + 1) and rock3(x * 2, t + 1)
#
# def rock4(x, t):
#     if x >= 26 and t == 3: return 1
#     elif x < 26 and t == 3: return 0
#     elif x >= 26 and t < 3: return 0
#     else:
#         if t % 2 == 0: return rock4(x + 1, t + 1) or rock4(x * 2, t + 1)
#         else: return rock4(x + 1, t + 1) or rock4(x * 2, t + 1)
#
# for i in range(1, 26):
#     if rock3(i, 1) and rock4(i, 1): print(i)





# def _17(f = open('./src/lab/1_17.txt')):
#     arr = [int(x) for x in f]
#     divs = [i for i in arr if 9 < i < 100]
#     res = []
#     for i in range(len(arr) - 1):
#         x, y = arr[i], arr[i + 1]
#         if ((x in divs and y not in divs) or (x not in divs and y in divs)) and sum([x, y]) % max(divs) == 0:
#             res.append(x + y)
#     return len(res), max(res)
#
# print(_17())

# def _22(f = open('./src/lab/22.csv')):
#     d = {'0': 0}
#     arr = [el.split(',') for el in f][1:]
#     for el in arr:
#         [key, time, dep] = el
#         dep = [int(elem) for elem in dep.split('; ')]
#         d[key] = max([d[f'{i}'] for i in dep]) + int(time)
#     return d
#
# print(_22())

# def _3(x, y):
#     if x == y: return 1
#     elif x > y: return 0
#     else: return _3(x + 1, y) + _3(x * 2, y)
# print(_3(2, 23))

# def _24(f = open('./src/lab/zadanie24_1.txt').readline()):
#     arr = f.replace('A', 'x')
#     arr = arr.replace('C', 'x')
#     arr = arr.split('x')
#     arr = [len(i) for i in arr]
#     return max(arr)
# print(_24())




# def _26(f = open('./src/lab/27886.txt')):
#     arr = [int(el) for el in f.readlines()[1:]]
#     arr = sorted(arr)
#     print(arr)
#     res, mx = [0], 0
#     for el in arr:
#         if sum(res) + el > 5955: break
#         else: res.append(el)
#     res = res[1:]
#     print(res)
#     if sum(res) < 5955:
#         for i in range(5955 - sum(res), 1, -1):
#             if (max(res) + i) in arr and (max(res) + i) > mx:
#                 mx = max(res) + i
#     return len(res), mx, sum(res)
# print(_26())


#
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

def _27_A(f = open('./src/lab/27-A-2.txt')):
    arr = sorted([int(el) for el in f][1:])
    lol = [el % 3 for el in arr]
    print(lol)

    return sum([arr[-2], arr[-3], arr[-5]])
#
# print(_27())
#
# print(_27_A())


#
#
#
def krab(n):
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True

# for x in range(101_000_000, 102_000_001, 2):
#     if ((x // 2) ** 0.5 == int((x // 2)** 0.5)) and krab((x // 2) ** 0.5):
#         pass
#
# print(101075762 ** 0.5, int(101075762 ** 0.5), krab(101075762 ** 0.5))
#












# def prime(n):
#     d = 2
#     while d * d <= n:
#         if n % d == 0: return False
#         d += 1
#     return True
#
# for x in range(101_000, 102_000, 2):
#     if ((x // 2) ** 0.5 == int((x // 2) ** 0.5)) and prime((x // 2) ** 0.5): print(x)


