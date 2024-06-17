import matplotlib.pyplot as plt

def lcg(a, c, m, n, k, x_0):
    x = [x_0]
    for i in range(k*n):
        x.append((x[-1] * a + c) % m)
    y = [i/m for i in x]
    ans = []
    for j in range(0,len(y),k):
        ans.append(y[j])
    return ans

data = lcg(16807, 0, 2**(31) - 1, 10000, 3, 0.5)
plt.hist(data,density = True)
