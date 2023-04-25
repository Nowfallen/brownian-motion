#library
import numpy as np
import matplotlib.pyplot as plt

#parameters 
num_steps=1000
dt=0.01
c=1

x=np.zeros(num_steps)
for i in range (0,num_steps-1):
#random force normalized
    n=np.random.normal(-1,1)
#using euler method to update the equation
    x[i+1]=x[i]+np.sqrt(c*dt)*n
#ploting
plt.plot(x)
plt.xlabel("nummber of steps")
plt.ylabel("position")
plt.title("overdumbed langevin simulation in 1D")
plt.grid()
plt.show()