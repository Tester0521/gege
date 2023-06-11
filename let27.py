f_a = open('./src/27-A.txt')
f_b = open('./src/27-B.txt')

def let27(f = f_a) -> print:
    arr = [int(el) for el in f][1:]
    gg = list(filter(lambda x: x > 0 and x % 2 == 0, arr))
    def shark(arr: list) -> list:
        c, cs = 0, []
        for i in arr:
            c += i
            if i % 2 == 0 and i > 0:
                cs.append(c)
                c = 0
        return cs

    wtf = arr[::-1]
    print(wtf)
    imposters, imposters2 = shark(arr[0:50]), shark(wtf[0:30])
    print(len(gg), sum(arr))
    print(imposters)
    print(imposters2)

    res = sum(arr)
    for i in range(6):
        x = min([imposters[i], imposters2[i]])
        if x == imposters[i]:
            imposters2 = imposters2[::-1]
            imposters2.append(0)
            imposters2 = imposters2[::-1]
        if x == imposters2[i]:
            imposters = imposters[::-1]
            imposters.append(0)
            imposters = imposters[::-1]
        res -= x

    print(res)

    print(sum(shark(arr)))

let27()


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