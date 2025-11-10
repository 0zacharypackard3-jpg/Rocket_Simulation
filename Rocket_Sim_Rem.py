#   pip install numpy scipy matplotlib

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


dt = 0.1
sim_time = 150
time = np.arange(0, sim_time + dt ,dt)

#Earth mass
earth_radius = 3963.19*1609.34  
mass_earth = 5.972 *10**24 
G = 6.674 * 10**-11 
g = (G * mass_earth) / (earth_radius)**2

rocket_mass = 199
upwards_force = 1959.655

height = 0
velocity = 0

velocity_list = []
height_list = []


for t in time:
    g = (G * mass_earth) / (earth_radius + height)**2
    delta_g = g - G * mass_earth / earth_radius**2
    rocket_weight = rocket_mass * g
    acceleration = (upwards_force - rocket_weight) / rocket_mass
    velocity += acceleration * dt
    height += velocity * dt
    velocity_list.append(velocity)
    height_list.append(height)



print()
force_required = rocket_mass * g

print(f"Required force for liftoff (N):", force_required )
print("height(m): ",height)

print()

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.plot(time, height_list, color="blue", label="Height (m)")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Height (m)", color="blue")
ax1.tick_params(axis='y', labelcolor="blue")
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(time, velocity_list, color="red", label="Velocity (m/s)")
ax2.set_ylabel("Velocity (m/s)", color="red")
ax2.tick_params(axis='y', labelcolor="red")

fig.tight_layout()
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
plt.title("Rocket_Simulation")
plt.show()
