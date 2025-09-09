import numpy as np

g = 9.81 #gravity
 
u = float(input("Enter initial speed of projectile: "))

while True: #loop to make sure angle is within range
    theta = float(input("Enter launch angle (0-90): "))
    if 0 <= theta <= 90:
        break
    else:
        print("Invalid launch angle, try again")
theta = float(np.radians(theta))

#quadratic equation to solve for t: -0.5gt^2 + usin(theta)t
a = (-0.5*g)
b = u*np.sin(theta)
c = 0

time_1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
time_2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)

t = (time_1 + time_2) #total time in the air
t_y_max = u*(np.sin(theta))/g

y_max = np.round((u*np.sin(theta)*t_y_max)-(0.5*g*((t_y_max)**2)), 2)

x_max = np.round((u*np.cos(theta)*t), 2)

print("The time spent your projectile spent in the air was " +str(np.round(t, 2)) + " seconds")
print("The maximun hight reached by your projectile was " + str(y_max) + " meters")
print("The horizontal distance traveled was " + str(x_max) + " meters")






