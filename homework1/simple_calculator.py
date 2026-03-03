num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

result = eval(f"{num1}{operation}{num2}")

print("Result: ", float(result))