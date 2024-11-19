import numpy as np
import matplotlib.pyplot as plt

def quadratic_function(x, A):
    return 0.5 * x.T @ A @ x

def plot_surface_contour_gradient(A, title):
    fig = plt.figure(figsize=(12, 8))


    ax = fig.add_subplot(121, projection='3d')
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[quadratic_function(np.array([xi, yi]), A) for xi, yi in zip(xi_row, yi_row)] for xi_row, yi_row in zip(X, Y)])
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.set_title(f'3D Surface - {title}')

    ax = fig.add_subplot(122)
    contour = plt.contour(X, Y, Z, 10, cmap='viridis')
    plt.title(f'Contour Lines - {title}')
    plt.colorbar(contour)

    plt.show()


A_minimum = np.array([[2, 0], [0, 3]])
A_maximum = np.array([[-2, 0], [0, -3]])
A_saddle = np.array([[1, 2], [2, 1]])


plot_surface_contour_gradient(A_minimum, 'Unique Minimum')
plot_surface_contour_gradient(A_maximum, 'Unique Maximum')
plot_surface_contour_gradient(A_saddle, 'Unique Saddle Point')
