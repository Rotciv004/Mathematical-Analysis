import numpy as np
import matplotlib.pyplot as plt

def generate_random_points(num_points):
    return np.random.uniform(low=-1, high=1, size=(num_points, 2))

def inside_unit_ball(point, p):
    return np.linalg.norm(point, ord=p) <= 1

def plot_unit_ball(p):
    num_points = 1000
    points = generate_random_points(num_points)

    inside_points = [point for point in points if inside_unit_ball(point, p)]
    outside_points = [point for point in points if not inside_unit_ball(point, p)]

    plt.scatter(*zip(*inside_points), color='blue', label='Inside Unit Ball')
    plt.scatter(*zip(*outside_points), color='red', label='Outside Unit Ball')

    plt.title(f'Unit Ball for p={p}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio for a circle
    plt.show()








p_values = [1.25, 1.5, 3, 8]

for p in p_values:
    plot_unit_ball(p)
