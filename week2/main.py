import numpy
import statistics
import math
from scipy import stats

x = [8.0, 1, 2.5, 4, 28.0]

print(x)

mean = sum(x) / len(x)
print(f"the manually calculated mean is {mean}")

mean2 = statistics.mean(x)
print(f"the auto calculated mean is {mean2}")

y = numpy.array(x)
mean3 = numpy.mean(y)
print(f"the numpy mean is {mean3}")

n = len(x)
if n%2:
    median = sorted(x)[round(0.5 * (n-1))]
else:
    xOrd = sorted(x)
    index = round(0.5*n)
    median = 0.5*(xOrd[index-1] + xOrd[index])

print(f"median is {median}")

median2 = statistics.median(x)
print(f"median using statistics is {median2}")

median3 = numpy.median(y)
print(f"median using numpy is {median3}")

u = [2,2,2,4,56,65,346,4357,365,2,2,5426,4357,4357,4357,4357,4357,4357,4357]
mode = max((u.count(item), item) for item in set(u))[1]
print(f"mode = {mode}")

mode2 = statistics.mode(u)
print(f"statistics mode = {mode2}")

w = numpy.array(u)
mode3 = stats.mode(w)[0]
print(f"scipy mode = {mode3}")