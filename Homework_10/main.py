import numpy as np
import matplotlib.pyplot as plt

def f(x, y, b):
    return 12 * (x**2 + b * y**2)

def gradient_descent(b, x0, y0, learning_rate, iterations):
    trajectory = []
    x, y = x0, y0
    for _ in range(iterations):
        trajectory.append((x, y))
        gradient = np.array([24 * x, 24 * b * y])
        x -= learning_rate * gradient[0]
        y -= learning_rate * gradient[1]
    return np.array(trajectory)

def plot_contours(b):
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y, b)

    plt.contour(X, Y, Z, levels=50, cmap='viridis')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Contour Plot of f(x, y) for b={b}')
    plt.grid(True)

b_values = [1, 12, 1/5, 10]
learning_rate = 0.1
iterations = 100

plt.figure(figsize=(12, 8))

for b in b_values:
    trajectory = gradient_descent(b, 1.5, 1.5, learning_rate, iterations)
    plt.plot(trajectory[:, 0], trajectory[:, 1], label=f'b={b}')

plot_contours(b_values[0])
plt.legend()
plt.show()
