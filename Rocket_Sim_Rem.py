#   pip install numpy scipy matplotlib

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


#Begin with the constants 
gravity = 9.8 
dt = 0.1

# Time for Thrust
srb = 7_500_000 - 1_200_000 
thrust_main = srb
ssme = 375_000 
thrust_minor = 3 * ssme
net_thrust = thrust_main + thrust_minor 
burn_time = 200 
sim_time = 300 
time = np.arange(0, sim_time +dt, dt)

#Velocity
acceleration = net_thrust * time
distance =  0.5 * acceleration * time**2
velocity = distance/time
V = velocity

#Drag D = .5 * cd *(rho V^2)/2 * A
cd = 0.78 # @ 40 degrees According to Reddit
rho = 1.225 #kg/m^3
A = 250 # m^2 the reference area of the shuttle was 2690 ft^2 = 250m^2
drag = 0.5 * cd * rho * V**2 / 2 * A


#lift= 21CLρvA
q = rho
S = A
cL = 1.2
lift = cL * (rho * V**2)/2 * A
# You need to further look at this its not good at all tbh. But it works for a place holder.


mass = (4_470_000)*2.2 #lbs times 2.2 equals kg
weight = mass * gravity  

#Time to make the rocket actually move
up_force = distance + lift
down_force = weight + drag
height = up_force - down_force

plt.figure(figsize =(12, 8)) #sizing of the figure
plt.plot(time, velocity, label="Velocity (m/s)")
plt.plot(time, height, label="Height (m)")
plt.xlabel("Time(s)")
plt.ylabel("Height")
plt.title("Space Shuttle Simulation")
plt.legend
plt.grid(True)
plt.show()




#The height is not realistic in my opinion as such I need to rewrite the upwards forces
#The overall code structure looks terrible, rewrite.
#But it did produce a working simulation even if entirely unrealistic and bad.
#Tommorow the improvements will be made

#Notes to self plot works fine, maybe add some color codes and another y axis to describe upwards force because I want to have a second stage to the burn_time
#After fix velocity  up_force and time during the plot.
#I think lift drag and weight are good though.
