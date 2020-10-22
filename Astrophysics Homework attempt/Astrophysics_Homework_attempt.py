import matplotlib.pyplot as plt
import numpy as np
#let x = r/Rs
#let y = p/p_0

#plot the effect of momentum vs radius for a star
x = np.arange(0.0001,10000,0.01)
y = (abs((1/(x*((1+x)*(1+x))))))

plt.subplot(222)
plt.plot(x,y)
plt.yscale('log')
plt.xscale('log')
plt.ylim(0,10000000)
plt.xlim(0,100)
plt.xlabel("log(r/Rs)")
plt.ylabel("log(p/p0)")
plt.show()



