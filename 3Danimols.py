import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter
from tqdm.auto import tqdm

# parameters
num_steps = 100
number_particles = 7
dt = 0.01
c = 1

# Initialize arrays for steps and positions
nx = np.zeros((number_particles, num_steps))
ny = np.zeros((number_particles, num_steps))
nz = np.zeros((number_particles, num_steps))
x = np.zeros((number_particles, num_steps))
y = np.zeros((number_particles, num_steps))
z = np.zeros((number_particles, num_steps))

# steps
for j in tqdm(range(number_particles), desc="Generating random walk data"):
    for i in range(num_steps - 1):
        nx[j, i] = np.random.normal(0, 1)
        ny[j, i] = np.random.normal(0, 1)
        nz[j, i] = np.random.normal(0, 1)
        
        # using Euler method to update the equation
        x[j, i + 1] = x[j, i] + np.sqrt(c * dt) * nx[j, i]
        y[j, i + 1] = y[j, i] + np.sqrt(c * dt) * ny[j, i]
        z[j, i + 1] = z[j, i] + np.sqrt(c * dt) * nz[j, i]

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Create a list of lines
lines = [ax.plot([], [], [], marker="o", markersize=5)[0] for _ in range(number_particles)]

ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min(), y.max())
ax.set_zlim(z.min(), z.max())
ax.set_xlabel("positionsX")
ax.set_ylabel("positionsY")
ax.set_zlabel("positionsZ")
ax.set_title("overdumbed langevin simulation (frame =5)(number of particles =7)")

def update(i):
    for j, line in enumerate(lines):
        line.set_data(x[j, i:i+1], y[j, i:i+1])
        line.set_3d_properties(z[j, i:i+1])
    return tuple(lines),

ani = FuncAnimation(fig, update, frames=num_steps, interval=20, blit=False)

# Save the animation as a GIF file
output_path = "/home/elaisati/Desktop/overdumbed langevin simulation.gif"
writer = PillowWriter(fps=5)
ani.save(output_path, writer=writer)

plt.show()


