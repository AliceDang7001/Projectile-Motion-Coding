# Import Packages
# ***************
import matplotlib.pyplot as plt
from numpy import pi, cos, sin


def CannonBallFLight():
    """

    :return:
    """

    # Constants
    theta = pi / 4  # degrees
    m = 10  # kg
    g = 9.81  # m/s^2
    d = 0.47  # Unitless
    rho = 1.275  # Density of air in kg/m^3
    A = .00950332  # m^2
    dt = 0.5  # s

    # Initial Conditions (No Drag)
    t = 0  # s
    v = 500  # m/s
    x = 0  # m
    h = 0  # m

    # Initial Conditions (Drag)
    td = 0  # s
    xd = 0  # m
    hd = 0  # m
    ax = 0  # m/s^2
    ay = 0  # m/s^2
    vx = v * cos(theta)  # m/s
    vy = v * sin(theta)  # m/s

    # Set up plot
    plt.title("Cannon Ball Flight")
    plt.xlabel("Distance in the x (m)")
    plt.ylabel("Distance in the y (m)")

    # Construct the legend
    plt.scatter(x, h, color="Green", label="No Air Resistance")
    plt.scatter(xd, hd, color="Blue", label="Air Resistance")
    plt.legend()

    # Main loop
    while h >= 0 or hd >= 0:

        # Crunch the numbers (No Drag)
        if h >= 0:
            t += dt

            x = v * cos(theta) * t

            h = v * sin(theta) * t - 0.5 * g * t ** 2

        # Crunch the numbers (Drag)
        if hd >= 0:
            td += dt

            xd += vx * dt
            vx += ax * dt
            ax = (-1 * d * rho * A * v * vx) / (2 * m)

            hd += vy * dt
            vy += (ay - g) * dt
            ay = (-1 * d * rho * A * v * vy) / (2 * m)

        # Plot
        plt.scatter(x, h, color="Green")
        plt.scatter(xd, hd, color="Blue")
        plt.show(block=False)
        plt.pause(0.000001)

    # Display results
    print("=" * 35)
    print("Time (No drag): ", t, "(s)")
    print("Distance (No drag): ", x, "(m)")
    print("-" * 35)
    print("Time (Drag): ", td, "(s)")
    print("Distance (Drag): ", xd, "(m)")
    print("=" * 35)

    # Final plot
    plt.scatter(x, h, color="Green")
    plt.scatter(xd, hd, color="Blue")
    plt.show()


# Main Execution
# **************
if __name__ == "__main__":
    CannonBallFLight()
