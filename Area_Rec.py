def calculate_rectangle_area(length, width):
    return length * width

# Taking user input for length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_rectangle_area(length, width)
print(f"The area of the rectangle with length {length} and width {width} is {area}.")
