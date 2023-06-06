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



def2()




