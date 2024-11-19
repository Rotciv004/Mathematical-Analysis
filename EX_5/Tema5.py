import numpy as np
import matplotlib.pyplot as plt

# Define a convex function f(x)
def convex_function(x):
    return x**2

# Define the gradient of the convex function f(x)
def gradient_convex_function(x):
    return 2*x

# Define a non-convex function g(x)
def nonconvex_function(x):
    return x**4 - 4*x**2

# Define the gradient of the non-convex function g(x)
def gradient_nonconvex_function(x):
    return 4*x**3 - 8*x

# Gradient Descent Algorithm
def gradient_descent(gradient, initial_x, learning_rate, num_iterations):
    x = initial_x
    x_history = [x]
    for _ in range(num_iterations):
        x = x - learning_rate * gradient(x)
        x_history.append(x)
    return x_history

# Helper function to plot the function and the convergence
def plot_convergence(f, gradient, x_history, title):
    x = np.linspace(-2, 2, 400)
    y = f(x)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='Function')
    plt.plot(x_history, [f(x) for x in x_history], 'ro-', label='Convergence')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Convex function with small learning rate
learning_rate_small = 0.1
initial_x = 1.5
convex_x_history_small = gradient_descent(gradient_convex_function, initial_x, learning_rate_small, 20)
plot_convergence(convex_function, gradient_convex_function, convex_x_history_small, 'Convex Function - Small Learning Rate')

# Convex function with large learning rate
learning_rate_large = 1.5
initial_x = 1.5
convex_x_history_large = gradient_descent(gradient_convex_function, initial_x, learning_rate_large, 20)
plot_convergence(convex_function, gradient_convex_function, convex_x_history_large, 'Convex Function - Large Learning Rate')

# Non-convex function with small learning rate
learning_rate_small = 0.01
initial_x = 1.5
nonconvex_x_history_small = gradient_descent(gradient_nonconvex_function, initial_x, learning_rate_small, 100)
plot_convergence(nonconvex_function, gradient_nonconvex_function, nonconvex_x_history_small, 'Non-Convex Function - Small Learning Rate')

plt.show()
