import numpy as np
import matplotlib.pyplot as plt

#establishing lists with initial conditions for values of x, y and t
x_displacements = [0]
y_displacements = [0]


#initial conditions
initial_y_disp = 0
initial_x_disp = 0
u = float(input("Enter the initial velocity "))
while True: #loop to make sure angle is within range
    theta = float(input("Enter launch angle (0-90): "))
    if 0 <= theta <= 90:
        break
    else:
        print("Invalid launch angle, try again")
theta = float(np.radians(theta))
g = 9.81
#other necessary things (most copied from version 1)
dt = 0.01

a = (-0.5*g)
b = u*np.sin(theta)
c = 0

time_1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
time_2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)

total_time = (time_1 + time_2) #total time in the air
iterations = int(total_time/dt) #how many iterations to do

#making a list of times which will be used for displacement calcs

times = [0]
t = 0
for i in range(iterations):
    t = np.round((t + dt), 2)
    times.append(float(t))

for t in times:
    y = (u*t*np.sin(theta))-(0.5*g*(t**2))
    y_displacements.append(float(y))
    x = (u*t*np.cos(theta))
    x_displacements.append(float(x))

fig,ax = plt.subplots()

ax.scatter(x_displacements, y_displacements, marker=',',s=1)
ax.set_xlabel("X-displacement")
ax.set_ylabel("Y-displacement")
plt.show()







