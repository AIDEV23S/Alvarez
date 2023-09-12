def primtal(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prim = [x for x in range(100) if primtal(x)]
print(f"primtalen är: {prim}")
#primtalen