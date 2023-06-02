from itertools import product as pr

def let8(arr: list = ['А', 'О', 'У']) -> str:
    arr = [list(x) for x in pr(arr, repeat = 5)]
    return arr[169]

print(let8())