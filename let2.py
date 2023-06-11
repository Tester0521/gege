from itertools import *




def let2() -> print:
    # №18808
    # f = lambda x, y, z, w: (x and not(y)) or (y == z) or w
    # ultra = [[[x1, x2, x3, 1], [1, x4, x5, x6], [1, 1, x7, x8]] for x1, x2, x3, x4, x5, x6, x7, x8 in product([0, 1], repeat = 8)]

    # 18071
    # f = lambda x, y, z, w: (x and not(y)) or (y == z) or not(w)
    # ultra = [[[0, x1, x2, 0], [0, 1, 0, 1], [x3, 1, 0, x4]] for x1, x2, x3, x4 in product([0, 1], repeat = 4)]

    # 27531
    # f = lambda x, y, z, w: not((x <= y) and (y != z) and (z or w))
    # ultra = [[[1, 1, x1, 1], [x2, 1, 1, x3], [1, x4, x5, x6]] for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat = 6)]

    # 16878
    # f = lambda x, y, z, w: (x != y) <= (z == (y or w))
    # ultra = [[[0, x1, 0, x2], [0, 0, x3, 0], [0, x4, x5, 0]] for x1, x2, x3, x4, x5 in product([0,1], repeat = 5)]

    # 27228
    # f = lambda x,y,z,w: not((not(x) or y or z) == (not(y) and z and w))
    # ultra = [[[x1, 1, 1, 1], [x2, 0, 0, x3], [x4, 1, x5, 1]] for x1, x2, x3, x4, x5 in product([0,1], repeat = 5)]

    for el in ultra:
        positions = [(x, y, z, w) for x, y, z, w in permutations(range(4)) if all(f(row[x], row[y], row[z], row[w]) == False for row in el)]
        if len(positions) == 1:
            (x, y, z, w) = positions[0]
            print(f'x: {x} y: {y} z: {z} w: {w}')
let2()