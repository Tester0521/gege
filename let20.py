def let20(s, s2, t):
    if s + s2 >= 47 and t == 4: return 1
    elif s + s2 < 47 and t == 4: return 0
    elif s + s2 >= 47 and t < 4: return 0
    else:
        if t % 2 != 0: return let20(s + 1, s2 + 2, t + 1) or let20(s + 2, s2 + 1, t + 1) or let20(s * 2, s2, t + 1) or let20(s, s2 * 2, t + 1)
        else: return let20(s + 1, s2 + 2, t + 1) and let20(s + 2, s2 + 1, t + 1) and let20(s * 2, s2, t + 1) and let20(s, s2 * 2, t + 1)

for i in range(1, 37):
    if let20(i, 10, 1) == 1: print(i)
