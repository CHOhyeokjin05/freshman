import numpy as np
import matplotlib.pyplot as plt

class numerical:
    def __init__(self,x):

        self.x = x
        self.initial = x[0]

    def f(self,x):    #self.x만 넣는 것이 아니라 다른 값도 넣을 수 있어야 함.
        return 9.8 * x + 0.5
    
    def numerical_derivative(self):
        h = 1e-4
        return (self.f(self.x + h)-self.f(self.x - h))/(2*h)
    
    def numerical_integral(self):
        total=0
        n=10000
        
        dx=(self.x - self.initial)/n


        for i in range(n):
            total += dx * self.f(self.initial + dx*(i+1))
        return total


x1 = np.linspace(0,10)
y1 = numerical(x1)

print(x1)
plt.plot(x1,y1.f(y1.x))
plt.plot(x1,y1.numerical_integral())
plt.show()


    