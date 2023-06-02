def let21(s, s2, t):
    if s + s2 >= 47 and (t == 5 or t == 3): return 1
    elif s + s2 < 47 and t == 5: return 0
    elif s + s2 >= 47 and t < 5: return 0
    else:
        if t % 2 == 0: return let21(s + 1, s2 + 2, t + 1) or let21(s + 2, s2 + 1, t + 1) or let21(s * 2, s2, t + 1) or let21(s, s2 * 2, t + 1)
        else: return let21(s + 1, s2 + 2, t + 1) and let21(s + 2, s2 + 1, t + 1) and let21(s * 2, s2, t + 1) and let21(s, s2 * 2, t + 1)
def let22(s, s2, t):
    if s + s2 >= 47 and t == 3: return 1
    elif s + s2 < 47 and t == 3: return 0
    elif s + s2 >= 47 and t < 3: return 0
    else:
        if t % 2 == 0: return let22(s + 1, s2 + 2, t + 1) or let22(s + 2, s2 + 1, t + 1) or let22(s * 2, s2, t + 1) or let22(s, s2 * 2, t + 1)
        else: return let22(s + 1, s2 + 2, t + 1) or let22(s + 2, s2 + 1, t + 1) or let22(s * 2, s2, t + 1) or let22(s, s2 * 2, t + 1)

for i in range(1, 37):
    if let21(i, 10, 1) == 1 and let22(i, 10, 1) == 1: print(i)