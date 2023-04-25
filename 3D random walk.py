#librabry
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# defining the number of steps and the time scale
num_steps = 1000
#steps
stepsx=np.random.choice([-1,1],size=num_steps)
stepsy=np.random.choice([-1,1],size=num_steps)
stepsz=np.random.choice([-1,1],size=num_steps)
#position
positionx=np.cumsum(stepsx)
positiony=np.cumsum(stepsy)
positionz=np.cumsum(stepsz)

time_steps=np.arange(num_steps)

#ploting
fig= plt.figure()
ax=fig.add_subplot(1,1,1,projection="3d")
ax.plot(positionx, positiony,positionz)
ax.set_xlabel("positionsX")
ax.set_ylabel("positionsY")
ax.set_zlabel("positionsZ")
ax.set_title("3D random walk simulation")
plt.show()
