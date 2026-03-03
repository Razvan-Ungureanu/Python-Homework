# Logical operators
print(True and False)
print(True or False)
print(not True)

# Bitwise operators
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(5 & 3)
print(5 << 3)
print(5 >> 3)

# Special operators
a = 5
print(a == 5)
print(a in [1, 2, 5])

x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

# Arithmetic operators
print(f"Sum: {x + y}")
print(f"Difference: {x - y}")
print(f"Product: {x * y}")
print(f"Division: {x / y}")
print(f"Floor Division (quotient): {x // y}")
print(f"Modulus (remainder): {x % y}")
print(f"Exponentiation (x to the power of y): {x ** y}")

# Special operators
number_list = [1, 2, 3, 5, 8, 13]

print(f"Is {x} in the list? {x in number_list}")
print(f"Is {y} missing from the list? {y not in number_list}")

name_1 = "Python"
name_2 = "Python"

print(f"Are they identical objects? {name_1 is name_2}")

# Logical operators
is_positive = x > 0
is_even = x % 2 == 0

print(f"Is the number both positive and even? {is_positive and is_even}")
print(f"Is the number either positive or even? {is_positive or is_even}")
print(f"The inverse of the 'even' state: {not is_even}")
