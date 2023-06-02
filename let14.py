def let14():
    x = 4**511 + 2**511 - 511
    res = bin(x)[2:]
    return res.count('1')

print(let14())