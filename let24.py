def let24(f = open('./src/24.txt')):
    s = f.readline()
    s = s.replace('ad', '8')
    s = s.replace('da', '8')
    arr = s.split('8')
    return max([len(el) for el in arr]) + 2

print(let24())