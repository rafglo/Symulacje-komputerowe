import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import random

def f(a, p):
    u = random.random()
    p_sum = 0

    for index in range(len(a)):
        p_sum += p[index]

        if (u < p_sum):
            return a[index]

a1 = 0
a2 = 0
a3 = 0
for i in range(1000):
    r = f([1,2,3], [0.5, 0.25, 0.25])

    if r == 1:
        a1 += 1
    elif r == 2:
        a2 += 1
    else:
        a3 += 1

# Histogram
plt.bar(['1', '2', '3'], [a1, a2, a3], color=['blue', 'green', 'red'])
plt.show()
