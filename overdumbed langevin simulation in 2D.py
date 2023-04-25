#library
import numpy as np
import matplotlib.pyplot as plt

#parameters 
num_steps=1000
dt=0.01
c=1

x=np.zeros(num_steps)
y=np.zeros(num_steps)

for i in range (0,num_steps-1):
#random force normalized
    ny=np.random.normal(0,1)
    nx=np.random.normal(0,1)
#using euler method to update the equation
    x[i+1]=x[i]+np.sqrt(c*dt)*nx
    y[i+1]=y[i]+np.sqrt(c*dt)*ny
    
#ploting
plt.plot(x,y)
plt.xlabel("positions x")
plt.ylabel("position y")
plt.title ("brawnian motrion in 2D using langevin equation")
plt.grid()
plt.show()