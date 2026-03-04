def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
    
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

def sum_list(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

def contains_number(numbers, target):
    if target in numbers:
        return True
    else:
        return False
    
print(is_even(4))
print(max_of_two(10, 7))
print(count_vowels("Hello World"))
print(sum_list([1, 2, 3, 4]))
print(contains_number([1, 2, 3, 4], 5))