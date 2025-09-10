import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#establishing lists with initial conditions for values of x, y and t
x_displacements = [0]
y_displacements = [0]


#initial conditions
initial_y_disp = 0
initial_x_disp = 0
while True: #loop to make sure angle is within range
    u = float(input("Enter the initial velocity (1-100)m/s: "))
    if u < 1:
        print("Initial velocity too low, try again ")
    elif u > 100:
        print("Initial velocity too High, try again ")
    else:
        break

while True: #loop to make sure angle is within range
    theta = float(input("Enter launch angle (0-90): "))
    if 0 <= theta <= 90:
        break
    else:
        print("Invalid launch angle, try again")
theta = float(np.radians(theta))
g = 9.81
#other necessary things (most copied from version 1)
dt = 0.1

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

#update to add quadratic best fit line
coefficients = np.polyfit(x_displacements, y_displacements, 2)
fit_fn = np.poly1d(coefficients)

x_smooth = np.linspace(min(x_displacements), max(x_displacements), 1000)
y_smooth = fit_fn(x_smooth)

u_max = 100
R_max = (u_max**2)/g
H_max = (u_max**2)/(2*g)

fig,ax = plt.subplots()

ax.set_xlim(0, R_max)
ax.set_ylim(0, H_max)
#ax.scatter(x_displacements, y_displacements, marker=',',s=1)
#ax.plot(x_smooth, y_smooth, 'r-', label="Quadratic Fit")
ax.set_xlabel("X-displacement (m)")
ax.set_ylabel("Y-displacement (m)")
ax.set_title("Projectile Motion Animation")

(projectile,) = ax.plot([], [], "bo", markersize=5) #The projectile
(path,) = ax.plot([], [], "r-", linewidth = 1.5) #The path-line drawn behind the projectile 

# functions for the animation
def init():
    projectile.set_data([], [])
    path.set_data([], [])
    return projectile, path

def update(frame):
    projectile.set_data([x_displacements[frame]], [y_displacements[frame]])
    path.set_data(x_displacements[:frame], y_displacements[:frame])
    return projectile, path


ani = FuncAnimation(fig, update, frames=len(times),
                    init_func=init, interval=10, blit=True, repeat=False)


plt.show()







