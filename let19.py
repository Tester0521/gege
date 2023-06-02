def let19(s, s2, t):
    if s + s2 >= 47 and t == 3: return 1
    elif s + s2 < 47 and t == 3: return 0
    elif s + s2 >= 47 and t < 3: return 0
    else: return let19(s + 1, s2 + 2, t + 1) or let19(s + 2, s2 + 1, t + 1) or let19(s * 2, s2, t + 1) or let19(s, s2 * 2, t + 1)

for i in range(1, 37):
    if let19(i, 10, 1) == 1: print(i)

