
import numpy as np
import matplotlib.pyplot as plt

num_steps = 1000
steps=np.random.choice([-1,1],size=num_steps)
positions=np.cumsum(steps)

time_steps=np.arange(num_steps)

plt.plot(time_steps, positions)
plt.xlabel("time steps")
plt.ylabel("position")
plt.title("1D Brawnian motion : random walk")
plt.grid()
plt.show()