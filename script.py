import sys

EPSILON = 1e-15  # Tolerance threshold for convergence

c = int(sys.argv[1])  
t = c  # Initialize the approximation with the input value

# Iterative process for finding the square root using Newton-Raphson method
while abs(t - c / t) > EPSILON:
    t = (c / t + t) / 2.0  # Update the approximation using the Newton-Raphson formula

print(t)  
