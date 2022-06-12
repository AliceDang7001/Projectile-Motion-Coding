# Import Packages
# ***************
import matplotlib.pyplot as plt
from numpy import arange, abs, pi, cos, sin, sqrt

def TheoryProjection():
    """

    :return:
    """

    # Constants
    theta = pi/12    # degrees
    m = 1            # kg
    g = 9.81         # m/s^2
    dt = 0.01       # s

    # Initial Conditions
    t = 0       # s
    v = 3.61    # m/s
    x = 0       # m
    h = 0       # m

    # Time Length Equation and velocity equation
    vx = v * cos(theta)
    vy = v * sin(theta)
    tl = (vy + sqrt(vy**2 + 2*g*h))/g

    # Set up plot
    plt.title("Projectile Motion")
    plt.xlabel("Distance in the x (m)")
    plt.ylabel("Distance in the y (m)")

    # Construct the legend
    plt.scatter(x, h, color="Green", label="No air resistance")
    # plt.scatter(x, h, color="Blue", label="Drag")
    plt.legend()


    # Main loop
    while t < tl:

        # Crunch the numbers
        x = vx*t
        h = vy*t - 0.5*g*t**2
        t += dt

        # Plot
        plt.scatter(x, h, color="Green")
        #plt.scatter(td, vd, color=colorDrag)
        plt.show(block=False)
        plt.pause(0.000001)

    # Display results
    print("=" * 35)
    print("Time (no drag): ", t)
    print("Distance (no drag): ", x)
    print("=" * 35)

    # Final plot
    plt.scatter(x, h, color="Green")
    plt.show()

# Main Execution
# **************
if __name__ == "__main__":
    TheoryProjection()