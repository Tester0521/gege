def let26(f = open('./src/26.txt')):
    parts = 500
    money = 4000000
    arr = [el.split() for el in f]
    arr = list(filter(lambda x: x[-1] == 'A', arr))
    arrB = list(filter(lambda x: x[-1] == 'B', arr))
    priceB= [int(el[0]) * int(el[1]) for el in arrB]
    money = money - sum(priceB)
    sorted_data = sorted(arr, key=lambda x: int(x[0]))
    quant = 0
    for el in sorted_data:
        money = money - int(el[0]) * int(el[1])
        quant += int(el[1])


    return money, quant



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

print(let26())