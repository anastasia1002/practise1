# cosx+cos^2x+...cos^nx
import math

n = int(input("натуральне число:"))
x = float(input("дійсне число:"))
sum = 0

for i in range(1,n+1):
    sum+=math.cos(x) ** i
print(sum)
