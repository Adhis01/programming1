import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c  # Calculate the discriminant

    # Check if the discriminant is positive, zero, or negative
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)  # First root
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)  # Second root
        print(f"The roots are real and different: {root1} and {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)  # One real root
        print(f"The root is real and the same: {root}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)  # Complex roots
        print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")

# Example usage:
solve_quadratic(1, -3, 2)  # For the equation x^2 - 3x + 2 = 0
