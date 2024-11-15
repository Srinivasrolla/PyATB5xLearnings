def classify_triangle(side1, side2, side3):
    # Check if the input values can form a triangle
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        # Classify the triangle
        if side1 == side2 == side3:
            return "The triangle is Equilateral."
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "The triangle is Isosceles."
        else:
            return "The triangle is Scalene."
    else:
        return "The given side lengths do not form a valid triangle."


# Input from the user
print("Enter the lengths of the three sides of the triangle:")
side1 = float(input("Side 1: "))
side2 = float(input("Side 2: "))
side3 = float(input("Side 3: "))

# Output the classification result
result = classify_triangle(side1, side2, side3)
print(result)
