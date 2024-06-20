import numpy as np
import matplotlib.pyplot as plt


def f(x, n):
    return 4*(-1)**n/(n**2*3.14**2)*np.cos(n*3.14*x)

def sum(x, n):
    sum = 0
    for i in range(1, n+1):
        sum += f(x, i)
        #print(sum,'\n')
    return sum
        
    
x = np.linspace(-3,3)
y = 1/3+sum(x, int(1e4))


plt.plot(x,y)
plt.show()