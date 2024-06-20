import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,10)
y = 2*x+3

x = np.append(x,0)
y = np.append(y,np.nan)

x = np.insert(x,6,0)
y = np.insert(y,6,np.nan)

print(x)
print(y)

plt.plot(x,y)
plt.show()