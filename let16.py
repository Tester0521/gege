def let16(n: int) -> int:
    if n == 1 or n == 2: return 1
    else: return let16(n - 2) * (n + 1)

print(let16(8))