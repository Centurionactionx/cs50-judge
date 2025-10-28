import numpy as np
import math

def f(x):
    return math.cos(3 * math.pi * x) - 0.5 * math.log(x, 7)

x_min, x_max = 1/49, 49
num_points = 1_000_000  
x_values = np.linspace(x_min, x_max, num_points)

y_values = [f(x) for x in x_values]

root_count = 0
for i in range(1, len(y_values)):
    if y_values[i-1] * y_values[i] < 0:
        root_count += 1

print(root_count)
