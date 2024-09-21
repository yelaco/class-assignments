import numpy as np
import matplotlib.pyplot as plt


def plot_points_and_points(points_1=None, points_2=None):
    """
    Plot points and/or a given function over the x-axis range determined by the points.

    Parameters:
    points (list of tuples): List of (x, y) points to be plotted.
    func (function): The function to plot.
    """
    plt.figure(figsize=(8, 6))

    # Plot points if provided
    if points_1:
        x_values = [point[0] for point in points_1]
        y_values = [point[1] for point in points_1]
        plt.plot(
            x_values, y_values, "b-", label="Data points"
        )  # Use 'b-' for blue line

        # Determine x-axis range based on points
        x_min = min(x_values)
        x_max = max(x_values)
        x_range = (x_min, x_max)

    if points_2:
        x_values = [point[0] for point in points_2]
        y_values = [point[1] for point in points_2]
        plt.plot(
            x_values, y_values, "r-", label="Estimated points"
        )  # Use 'b-' for blue line

        # Determine x-axis range based on points
        x_min = min(x_values)
        x_max = max(x_values)
        x_range = (x_min, x_max)

    # Add title and labels
    plt.title("Plot")
    plt.xlabel("x")
    plt.ylabel("y")

    # Add a legend
    plt.legend()

    # Show grid
    plt.grid(True)

    # Display the plot
    plt.show()


def solve(initial_value, a, b, N, f):
    h = (b - a) / N
    result = [[0.0, 0.0] for _ in range(N + 1)]
    result[0][0] = a
    result[0][1] = initial_value
    for i in range(1, N + 1):
        result[i][0] = a + i * h
        result[i][1] = result[i - 1][1] + h * f(a + (i - 1) * h, result[i - 1][1])
    return result


initial_value = [1, -1 / np.log(2), -2, 1]
a = [0, 1, 1, 0]
b = [1, 2, 3, 1]
N = [10, 10, 10, 10]
f = [
    lambda t, y: (2 - 2 * t * y) / (t**2 + 1),
    lambda t, y: y**2 / (1 + t),
    lambda t, y: (y**2 + y) / t,
    lambda t, y: -t * y + 4 * t / y,
]

problems = ["a", "b", "c", "d"]
for i, problem in enumerate(problems):
    print(f"\nSolving problem ({problem})")
    euler_result = solve(initial_value[i], a[i], b[i], N[i], f[i])

    plot_points_and_points(euler_result)
