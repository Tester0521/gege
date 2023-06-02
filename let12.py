def let12(s: str) -> str:
    while '11111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)
    return s
print(let12('1'*80))