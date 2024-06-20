import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1/x


def numerical_derivative(x):
    h=1e-4
    return (f(x+h)-f(x-h))/(2*h)


def numerical_integral(x):
    total=0
    n=10000
    dx=x/n


    for i in range(n):
        total += dx*f(dx*(i+1))
    return total



x=np.linspace(-10,10)
y=f(x)
dy=numerical_derivative(x)
iy=numerical_integral(x)
   


'''
좀 더 강력한 수렴 기준 필요!!!!
error : invalid convergence criteria

for i in range(len(dy)):
    if abs(dy[i]-dy[0])<1e-6:
        dy[i]=dy[0]
    else:
        break
'''

if abs((f(x[-1])-f(x[0]))/(x[-1]-x[0]) - dy[0]) < 1e-6:
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
axes[0].plot(x,y,'red',label='f(x)')
axes[1].plot(x,dy,label='derivative f(x)')
axes[2].plot(x,iy,'green',label='integral f(x)')

for i in range(3):
    axes[i].spines['right'].set_visible(False)
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['bottom'].set_position(('data',0))
    axes[i].spines['left'].set_position(('data',0))
    axes[i].grid()
    axes[i].legend()

axes[1].legend(loc=9)


plt.show()