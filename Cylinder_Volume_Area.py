import math

def calculate_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def calculate_cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height


radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
surface_area = calculate_cylinder_surface_area(radius, height)
volume = calculate_cylinder_volume(radius, height)
print(f"The surface area of the cylinder is {surface_area}.")
print(f"The volume of the cylinder is {volume}.")
