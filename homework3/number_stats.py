def number_stats(numbers):
    if len(numbers) == 0:
        return "No numbers given"
    
    smallest = min(numbers)
    largest = max(numbers)
    average = sum(numbers) / len(numbers)

    odd_count = 0
    for num in numbers:
        if num % 2 != 0:
            odd_count += 1

    print("Smallest:", smallest)
    print("Largest:", largest)
    print("Average:", average)
    print("Odd numbers:", odd_count)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    number_stats(numbers)