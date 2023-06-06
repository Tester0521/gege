
from sys import *
from functools import lru_cache
setrecursionlimit(110000)


@lru_cache(maxsize=128)
def let23(x: int, y: int) -> int:
    if x == y: return 1
    if x == 30 or x > y: return 0
    else: return let23(x + 1, y) + let23(x * 2, y) + let23(x * 3, y)

print(let23(2, 12) * let23(12, 36))