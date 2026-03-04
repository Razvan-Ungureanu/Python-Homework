def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)
    
    return result

def oldest_person(people):
    oldest = people[0]
    
    for person in people:
        if person[1] > oldest[1]:
            oldest = person
    
    return oldest[0]

def most_frequent(numbers):
    max_count = 0
    most_common = None

    for num in numbers:
        count = numbers.count(num)

        if count > max_count:
            max_count = count
            most_common = num

    return most_common

if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

    people = [("Ana", 25), ("Ion", 30), ("Maria", 28)]
    print(oldest_person(people))

    print(most_frequent((1, 2, 2, 3, 3, 3, 4)))