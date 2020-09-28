# Importing important modules
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


# Functions that returns dz/dt:

def model(theta, t, b, g, l, m):
    theta1 = theta[0]
    theta2 = theta[1]

    dtheta1_dt = theta2
    dtheta2_dt = -(b / m) * theta2 - (g / l) * math.sin(theta1)

    dtheta_dt = [dtheta1_dt, dtheta2_dt]
    return dtheta_dt


b = 0.05
g = 9.81
l = 1
m = 1

# Initial condition

theta_0 = [0, 3]

# Time points
t = np.linspace(0, 20, 150)

# solve ODE
# odient function from Scipy module. It is function that integrate systems of differential equcation.

theta = odeint(model, theta_0, t, args=(b, g, l, m))

# Plot results

plt.plot(t, theta[:, 0], 'b-', Label=r'$\frac{d\theta_1}{dt}=\theta2$')
plt.plot(t, theta[:, 1], 'r--', Label=r'$\frac{d\theta2}{dt}=-\frac{b}{m}\theta_2-\frac{g}{L}sin\theta_1$')

plt.ylabel('Displacement')
plt.xlabel('Time')
plt.legend()
plt.show()

# Counter

ct = 1

for t1 in theta[:, 0]:
    # initial Co-ordinates for fixed point
    x0 = 0
    y0 = 0

    # End Co-ordinates for string
    x1 = l * math.sin(t1)
    y1 = -l * math.cos(t1)

    filename = str(ct) + '.png'

    ct = ct + 1

    plt.figure()

    # Plotting Horizontal line

    plt.plot([-0.5, 0.5], [0, 0], 'g', linewidth=5)

    # Plotting String of Pendulum
    plt.plot([x0, x1], [y0, y1], 'r')

    # Plotting Ball of Pendulum
    plt.plot(x1, y1, 'o', markersize=30)

    # Limiting X - axis
    plt.xlim([-1.5, 1.5])

    # Limiting Y- axis
    plt.ylim([-1.5, 1.5])

    # Title
    plt.title('Simple Pendulum Animation using Python')

    plt.savefig(filename)