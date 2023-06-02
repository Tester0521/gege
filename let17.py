

def let17(f = open('src/17.txt')):
    arr = [int(el) for el in f]
    res = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if (arr[i] % 160 != arr[j] % 160) and (arr[i] % 7 == 0 or arr[j] % 7 == 0):
                res.append(arr[i] + arr[j])
                c += 1
    return len(res), max(res)

print(let17())