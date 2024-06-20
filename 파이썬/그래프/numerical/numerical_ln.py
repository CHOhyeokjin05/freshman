import numpy as np
import matplotlib.pyplot as plt
import warnings


def f(x):
    return 1/x

def numerical_derivative(x):
    h=1e-4
    return (f(x+h)-f(x-h))/(2*h)


def numerical_integral(x):
    total=0
    n=10000
    dx=(x-x[0])/n


    for i in range(n):
        total += dx*f(x[0]+dx*(i+1))
    return total


x_fake = np.linspace(-10,10)

warnings.filterwarnings('error', category=RuntimeWarning)

del_list = []


for i in range(len(x_fake)):
    try:

        iy = numerical_integral(x_fake[i])
        
    except:
        
        del_list.append(i)


x3 = np.delete(x_fake, del_list,axis=None)
del_list = []


for i in range(len(x_fake)):
    try:


        y = f(x_fake[i])

        
    except:
        
        
        del_list.append(i)
x1 = np.delete(x_fake, del_list,axis=None)
del_list=[]


for i in range(len(x_fake)):
    try:

        dy = numerical_derivative(x_fake[i])
        
    except:
        
        del_list.append(i)
x2 = np.delete(x_fake,del_list,axis=None)



if not list(x1):
    x1 = np.linspace(1e-1,10)

if not list(x2):
    x2 = np.linspace(1e-1, 10)

if not list(x3):
    x3 = np.linspace(1e-1,10)

y = f(x1)
dy = numerical_derivative(x2)
iy = numerical_integral(x3)


'''
좀 더 강력한 수렴 기준 필요!!!!
error : invalid convergence criteria

for i in range(len(dy)):
    if abs(dy[i]-dy[0])<1e-6:
        dy[i]=dy[0]
    else:
        break
'''

if abs((f(x1[-1])-f(x1[0]))/(x1[-1]-x1[0]) - dy[0]) < 1e-6:
    for i in range(len(dy)):
        dy[i]=dy[0]

'''

fig=plt.figure()

ax1 = fig.add_subplot(311)
ax1.plot(x,y)

ax2 = fig.add_subplot(312)
ax2.plot(x,dy)

ax3 = fig.add_subplot(313)
ax3.plot(x,iy)

plt.show()
'''
#행 개수를 1로 설정했기 때문에 [0, 0] 안 됨.
fig, axes = plt.subplots(1,3)
axes[0].plot(x1,y,'red',label='f(x)')
axes[1].plot(x2,dy,label='derivative f(x)')
axes[2].plot(x3,iy,'green',label='integral f(x)')

for i in range(3):
    axes[i].spines['right'].set_visible(False)
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['bottom'].set_position(('data',0))
    axes[i].spines['left'].set_position(('data',0))
    axes[i].grid()
    axes[i].legend()

axes[1].legend(loc=9)

plt.show()