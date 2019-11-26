#x=2(sin(x)-sin2x/2+sin3x/3+...(-1)^n-1 sin xn/n
import math
x = float(input("Введіть число:"))
eps = float(input("Epsilont:"))
sum = 0
k = 1
q = 1
while math.fabs(math.sin(k * x) / k) > eps:
    sum += q * math.sin(k * x) / k
    k += 1
    q *= -1
print (sum, x, eps)
