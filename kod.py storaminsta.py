import math
största = 0
minsta = 1.e300
while True:
    tal = float(input(">"))
    if tal < 0:
        break
    if tal > största:
        största = tal
    if tal < minsta:
        minsta = tal
print(f"största talet: {största}")
print(f"minsta talet: {minsta}")

