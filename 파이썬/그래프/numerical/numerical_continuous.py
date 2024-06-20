import numpy as np
import matplotlib.pyplot as plt



def f(x):
    with np.errstate(divide='ignore',invalid='ignore'):
        return 1/np.tan(x)
    


def numerical_derivative(x):
    h=1e-7
    return (f(x+h)-f(x-h))/(2*h)


def numerical_integral(x):
    total=0
    n=10000
    dx=(x-x[0])/n


    for i in range(n):
        total += dx*f(x[0]+dx*(i+1))
    return total


x = np.linspace(-6.28,6.28,100000)
y = f(x)
del_list = []

for i in range(1,len(x)-1):
    
    if (f(x[i])-f(x[i-1])) * (f(x[i+1])-f(x[i])) < 0 and numerical_derivative(x[i+1])*numerical_derivative(x[i]) > 10:
        del_list.append(i+1)


x = np.insert(x, del_list, np.nan)
y = np.insert(y, del_list, np.nan)

print(del_list)
print(x[24987:24990])
print(f(x[24987:24990]))
print(numerical_derivative(x[24987:24990]))
fig, axes = plt.subplots(1,1)
axes.plot(x,y,label='f(x)')
#axes.scatter(x,y)
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
axes.spines['left'].set_position(('data',0))
axes.spines['bottom'].set_position(('data',0))
axes.grid()
axes.legend()
axes.set_ylim(-30,30)
axes.set_xticks(np.arange(x[0],x[-1],np.pi))


plt.show()
