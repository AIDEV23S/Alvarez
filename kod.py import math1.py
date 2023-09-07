import math
t = int(input("antal år? "))
lam = math.log(2.0) / 5730
n0 = 100
rest = n0 * math.exp(-lam * t)
print(f"det återstår {rest: 1f} % ")
