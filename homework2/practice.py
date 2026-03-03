# 1. Pozitiv, negativ sau zero
number = float(input("Enter a number: "))

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

# 2. Par sau impar
number2 = int(input("\nEnter a number: "))

if number2 % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# 3. Vocala sau consoana
letter = input("\nEnter a letter: ")

if letter.lower() in "aeiou":
    print("It is a vowel")
else:
    print("It is a consonant")

# 4. Reducere varsta
age = int(input("\nEnter your age: "))

if age < 18 and age > 65:
    print("You get a discount")
else:
    print("No discount")

# 5. An bisect
year = int(input("\nEnter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")