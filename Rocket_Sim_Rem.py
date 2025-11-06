#Begin with the constants 
g = 9.8 #Gravity 

# Time for Thrust
srb = 7_500_000 - 1_200_000 #Solid Rocket Booster in KG aswell
thrust_main = srb
ssme = 375_000 # Space Shuttle Main Engines also in KG
thrust_minor = 3 * ssme
net_thrust = thrust_main + thrust_minor # #Up is good thrust make go up
burn_time = 200 # not sure what to put here yet. Lets assume 200 seconds for now
sim_time = 300 # has to be larger than burn_time because we dont want a instant velocity.
t = sim_time


# Overall distance should be D= A*T where a is constant acceleration and t is just time.
acceleration = net_thrust * t # overall positive forces mulitplied by the time they are acting
d = acceleration * t
velocity = d/t
V = velocity # V is total average velocity which is described as distance / time


#Drag is described by D = cd * (I think) (rho V^2)/2 * A
cd = 0.78 # @ 40 degrees According to Reddit
rho = 1920 #kg/m^3
A = 250 # m^2 the reference area of the shuttle was 2690 ft^2 = 250m^2
drag = cd * rho * V**2 / 2 * A

#L= 21CLρvA

#as such we have to move onto lift.
q = rho
S = A
cL = 1.2
L = cL * (rho * V**2)/2 * A
# You need to further look at this its not good at all tbh. But it works for a place holder.


mass = 4_470_000 #lbs approximate weight of the filled space shuttle
weight = mass * g  #Weight is the force of gravity applied to the mass of an object 
#Also weight will be represented in newtons (N) , while mass will be represented in kilograms (KG) because science is good,
dt = 0.1 # since we want an accurate plot the times checked will be a tenth instead of one unit.


# I am exhausted I believe most of the calculations are a good starting point but I have class


# Also github has both been great and terrible to use at the same time. I hope I dont have to spend another hour fixing the codespace tommorow.
