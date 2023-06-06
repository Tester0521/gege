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

print(let26())