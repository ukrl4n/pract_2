import numpy as np

# Вхідні дані
x_values = [0.1, 0.3, 1.5, 1.3, 1.8, 2.6]
y_values = [1.10517, 1.64872, 2.22554, 3.6693, 6.04965, 13.4637]

def lagrange_interpolation(x, x_points, y_points):
    L = 0
    n = len(x_points)
    for i in range(n):
        li = 1
        for j in range(n):
            if i != j:
                li *= (x - x_points[j]) / (x_points[i] - x_points[j])
        L += y_points[i] * li
    return L

# Інтерполяція другого степеня
x_points_deg2 = x_values[:3]
y_points_deg2 = y_values[:3]

# Інтерполяція третього степеня
x_points_deg3 = x_values[:4]
y_points_deg3 = y_values[:4]

# Точки для обчислення наближених значень
x_test_points = [0.3, 1.5]

# Обчислення значень
results_deg2 = [lagrange_interpolation(x, x_points_deg2, y_points_deg2) for x in x_test_points]
results_deg3 = [lagrange_interpolation(x, x_points_deg3, y_points_deg3) for x in x_test_points]

# Вивід результатів
print("Інтерполяційний многочлен другого степеня:")
for x, y in zip(x_test_points, results_deg2):
    print(f"f({x}) ≈ {y}")

print("\nІнтерполяційний многочлен третього степеня:")
for x, y in zip(x_test_points, results_deg3):
    print(f"f({x}) ≈ {y}")
