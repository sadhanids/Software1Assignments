import random

N = int(input("Enter the number of random points to generate: "))
points_inside_circle = 0
for i in range(N):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2 + y**2 < 1:
        points_inside_circle += 1

    pi_estimate = 4 * points_inside_circle / N

print(f"Approximation of pi:{pi_estimate:.2f}")



