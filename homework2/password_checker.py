password = input("Enter your password: ")

has_uppercase = False
has_number = False
for char in password:
    if char.isupper():
        has_uppercase = True
    if char.isdigit():
        has_number = True

if len(password) >= 8 and has_uppercase and has_number:
    print("Password is strong")
else:
    print("Password too weak")