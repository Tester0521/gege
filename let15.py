
def let15():
    def f(n, m) -> bool: return n % m == 0
    for A in range(1, 100100):
        for x in range(1, 100001):
            if not( f(90, A) and ( (not(f(x, A))) <= ( f(x, 15) <= (not(f(x, 20))) ) ) ): break
        else: print(A)
let15()