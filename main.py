import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 500)
x = np.sin(t)

plt.plot(t, x)
plt.xlabel("time")
plt.ylabel("position")
plt.title("numpy + matplotlib working")
plt.show()
