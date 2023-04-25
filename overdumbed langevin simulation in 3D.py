#library
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#parameters 
num_steps=1000
dt=0.01
c=1

x=np.zeros(num_steps)
y=np.zeros(num_steps)
z=np.zeros(num_steps)

for i in range (0,num_steps-1):
#random force normalized
    nx=np.random.normal(0,1)
    ny=np.random.normal(0,1)
    nz=np.random.normal(0,1)
    
#using euler method to update the equation
    x[i+1]=x[i]+np.sqrt(c*dt)*nx
    y[i+1]=y[i]+np.sqrt(c*dt)*ny
    z[i+1]=z[i]+np.sqrt(c*dt)*nz
    
# Plot the motion in 3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('position X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Motion with Overdamped Langevin Equation ')
plt.show()