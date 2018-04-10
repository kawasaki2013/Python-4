# coding: utf-8

# Area calculation program

print("Welcome to the Area calculation program")
print("---------------------------------------")
print()

# Print out the menu:
print("Please select a shape:")
print("1  Rectangle")
print("2  Circle")

# Get the user's choice:
shape = input("> ")
print(shape)

# Calculate the area:
if shape == "1":
    height = input("Please enter the height: ")
    width = input("Please enter the width: ")
    area = int(height) * int(width)
    print()
    print("The area is", area)
else:
    radius = input("Please enter the radius: ")
    area = 3.14*(int(radius)**2)
    print()
    print("The area is", area)
