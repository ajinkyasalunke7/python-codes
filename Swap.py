def swap_variables(a, b):
    a, b = b, a
    return a, b

# Taking user input for two variables
var1 = input("Enter the value of variable 1: ")
var2 = input("Enter the value of variable 2: ")

print(f"Before swapping: Variable 1 = {var1}, Variable 2 = {var2}")
var1, var2 = swap_variables(var1, var2)
print(f"After swapping: Variable 1 = {var1}, Variable 2 = {var2}")
