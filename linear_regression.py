import numpy as np
import matplotlib.pyplot as plt

x = [20,21,22,23,24,25,26,27,28,29]  # age
y = [3,3.5,2,5,7,6,4,7.6,9,10]#  monthly salary

fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit)

print (fit)
print(fit_fn)

plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
plt.xlim(17, 35)
plt.ylim(0, 15)
plt.show()