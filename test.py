from math import exp, cos, sin

def fun(x):
    return exp(x/cos(sin(x)))

xs = []
ys = []

for i in range(10000):
    x = i/1000
    xs.append(x)
    ys.append(fun(x))

import matplotlib.pyplot as plt

plt.plot(xs,ys)
plt.show()
