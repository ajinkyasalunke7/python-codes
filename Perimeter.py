def calculate_square_area(side):
    return side ** 2

def calculate_square_perimeter(side):
    return 4 * side

# Taking user input for side length of the square
side_length = float(input("Enter the side length of the square: "))
area = calculate_square_area(side_length)
perimeter = calculate_square_perimeter(side_length)
print(f"The area of the square with side length {side_length} is {area}.")
print(f"The perimeter of the square with side length {side_length} is {perimeter}.")
