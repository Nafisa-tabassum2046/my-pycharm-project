# Triangle Area of plane shapes

base = float(input("Enter the base value: "))
height = float(input("Enter the height value: "))
Triangle_area = 0.5 * base* height
print("The Triangle_area is: ",Triangle_area)

# Rectangle Area of plane shapes

Width = float(input("Enter the width value: "))
# height = float(input("Enetr height value: "))
Rectangle_Area = Width * height
print("The Rectangle Area is :", Rectangle_Area)

# Trapezoid Area of plane shapes

a = float(input("Enter the a value: "))
b = float(input("Enter the b value: "))
# height = float(input("Enter the height value: "))
Trapezoid_Area = 0.5 * (a+b) * height
print("Triangle_area is :", Trapezoid_Area)

# Ellipse Area of plane Shapes

Ellipse_Area = 3.1416 * a * b
print("Ellipse_Area is: ",Ellipse_Area )

# Square Area pf plane Shapes
Square_Area = a*a
print("Square_Area is: ", Square_Area)

#  Parallelogram Area of plane Shapes

Parallelogram_Area = base * height
print("Parallelogram Area is :", Parallelogram_Area)

#  Circle Area of plane Shapes

radius = float(input("Enter the radius value :"))
Pi = 3.1416
Cricle_Area = Pi * radius *radius
print("Cricle Area is: ", Cricle_Area)

#  Sector Area of plane Shapes

radius_of_angle = float(input("Enter the angle value: "))
Sector_Area = 0.5 * radius * radius * radius_of_angle
print("Sector Area is : ", Square_Area)
