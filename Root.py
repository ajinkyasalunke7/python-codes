import math

def find_square_root(number):
    return math.sqrt(number)

# Taking user input for a number
num = float(input("Enter a number to find its square root: "))
square_root = find_square_root(num)
print(f"The square root of {num} is {square_root}.")
