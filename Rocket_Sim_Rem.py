#   pip install numpy scipy matplotlib

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


dt = 0.1
sim_time = 1200
time = np.arange(0, sim_time + dt ,dt)

#Earth mass
earth_radius = 3963.19*1609.34  
mass_earth = 5.972 *10**24 
G = 6.674 * 10**-11 
g = (G * mass_earth) / (earth_radius)**2
surface_g = (G * mass_earth) / (earth_radius)**2


initial_rocket_mass = 20000
fuel_burn_rate = 100
mj_kg = 140
fuel_mass = 700
exhaust_velocity = 3000

total_energy = mj_kg* 1e6 * fuel_mass
burn_time = fuel_mass / fuel_burn_rate
power = total_energy / burn_time
thrust_force = power / exhaust_velocity

def thrust(fuel_mass_remaining):
    if fuel_mass_remaining > 0:
        return thrust_force
    else:
        return 0

height = 0
velocity = 0

solid_mass = initial_rocket_mass - fuel_mass

apogee_height = None
velocity_list = []
height_list = []


for t in time:
    g = (G * mass_earth) / (earth_radius + height)**2

    delta_g = g - G * mass_earth / earth_radius**2

    fuel_mass -= fuel_burn_rate * dt
    fuel_mass = max(fuel_mass, 0)


    rocket_mass =solid_mass + fuel_mass
    rocket_weight = rocket_mass * g

    upwards_force =thrust(fuel_mass)

    acceleration = (upwards_force - rocket_weight) / rocket_mass

    velocity += acceleration * dt
    height += velocity * dt
    velocity_list.append(velocity)
    height_list.append(height)
    if velocity <0 and apogee_height is None:
        apogee_height = height
    if apogee_height is not None and height <= 0:
        height = 0
        break

time_truncated = time[:len(height_list)]


print()
force_required = initial_rocket_mass * surface_g

print(f"Required force for liftoff (N):", force_required )
print("height(m): ",height)
print("Apogee detected at ", apogee_height)

print()

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.plot(time_truncated, height_list, color="blue", label="Height (m)")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Height (m)", color="blue")
ax1.tick_params(axis='y', labelcolor="blue")
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(time_truncated, velocity_list, color="red", label="Velocity (m/s)")
ax2.set_ylabel("Velocity (m/s)", color="red")
ax2.tick_params(axis='y', labelcolor="red")

fig.tight_layout()
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
plt.title("Rocket_Simulation")
plt.show()
 