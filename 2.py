import numpy as np
import matplotlib.pyplot as plot


x=np.arange(0,5,0.01)
y=np.sin(x)

plot.plot(x,y)
plot.set(xlabel='time(s)',ylabel='sin(x)',title='SIN(X)')
plot.show()
