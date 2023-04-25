#library
import numpy as np
import matplotlib.pyplot as plt

# defining the number of steps and the time scale
num_steps = 1000
#steps
stepsx=np.random.choice([-1,1],size=num_steps)
stepsy=np.random.choice([-1,1],size=num_steps)
#position
positionx=np.cumsum(stepsx)
positiony=np.cumsum(stepsy)


time_steps=np.arange(num_steps)

#ploting
plt.plot(positionx, positiony)
plt.xlabel("xposition")
plt.ylabel("yposition")
plt.title("2D Brawnian motion: random walk")
plt.grid()
plt.show()