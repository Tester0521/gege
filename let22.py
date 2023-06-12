

def let22(f = open('./src/22_12.csv')):
    arr = [el.split(',') for el in f][1:]
    d = {'0': 0}
    for el in arr:
        key, time, follows = el[0], int(el[1]), list(map(int, filter(lambda x: x != '', el[-1].split(';'))))
        d[key] = max([d[f'{i}'] for i in follows]) + time
    return max(d.values())

print(let22())


def csv22(f = open('./src/lab/22csv.csv')):
    arr = [el for el in f][1:]
    d = {'0': 0}
    for el in arr:
        [key, time, dep] = el.split(',')
        dep = dep.replace('\n', '')
        dep = dep.split(';')
        if dep[0] == '':
            dep[0] = '0'
            d[key] = int(time)
        else: d[key] = max([int(d[x]) for x in dep]) + int(time) + 3
    return max(d.values())