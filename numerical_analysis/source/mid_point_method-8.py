import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(10)


def plot_points(points_1=None, points_2=None, points_3=None, points_4=None):
    """
    Plot points and/or a given function over the x-axis range determined by the points.

    Parameters:
    points_1, points_2, points_3, points_4 (list of tuples): Lists of (x, y) points to be plotted.
    """
    plt.figure(figsize=(8, 6))

    x_range = [float("inf"), float("-inf")]

    # Plot points if provided
    if points_1:
        x_values = [point[0] for point in points_1]
        y_values = [point[1] for point in points_1]
        plt.plot(x_values, y_values, "b-", label="Data points")
        x_range[0] = min(x_range[0], min(x_values))
        x_range[1] = max(x_range[1], max(x_values))

    if points_2:
        x_values = [point[0] for point in points_2]
        y_values = [point[1] for point in points_2]
        plt.plot(x_values, y_values, "r-", label="Estimated points")
        x_range[0] = min(x_range[0], min(x_values))
        x_range[1] = max(x_range[1], max(x_values))

    # Add title and labels
    plt.title("Plot of Multiple Point Sets")
    plt.xlabel("x")
    plt.ylabel("y")

    # Add a legend
    plt.legend()

    # Show grid
    plt.grid(True)

    # Set x-axis range
    plt.xlim(x_range)

    # Display the plot
    plt.show()


def f(x, y):
    pass


# Input
# initial_value: y(a)
# a, b: boundaries
# N: intervals
# f: differential function
# s: actual solution
def mid_point_method(initial_value, a, b, N, f, s):
    approximation = np.zeros(shape=(N + 1,))
    actual_result = np.zeros(shape=(N + 1,))
    plot_approx = []
    plot_actual = []
    h = (b - a) / N
    for i in range(N + 1):
        if i == 0:
            approximation[i] = initial_value
            actual_result[i] = initial_value
        else:
            temp = approximation[i - 1] + h / 2 * f(
                a + (i - 1) * h, approximation[i - 1]
            )
            approximation[i] = approximation[i - 1] + h * f(a + (i - 1 / 2) * h, temp)
            actual_result[i] = s(a + i * h)
            plot_approx.append((a + i * h, approximation[i]))
            plot_actual.append((a + i * h, actual_result[i]))
    plot_points(plot_actual, plot_approx)
    print("Approximation:", approximation)
    print("Actual result:", actual_result)
    print("Errors:", np.abs(approximation - actual_result))
    print("MSE:", np.sum((approximation - actual_result) ** 2) / (N + 1))


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
s = [
    lambda t: (2 * t + 1) / (t**2 + 1),
    lambda t: -1 / np.log(t + 1),
    lambda t: 2 * t / (1 - 2 * t),
    lambda t: np.sqrt(4 - 3 * np.exp(-(t**2))),
]

problems = ["a", "b", "c", "d"]
for i, problem in enumerate(problems):
    print(f"\nSolution for problem ({problem}):")
    mid_point_method(initial_value[i], a[i], b[i], N[i], f[i], s[i])
