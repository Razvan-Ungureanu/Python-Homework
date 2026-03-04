def analyze_people(people):
    oldest_name = None
    oldest_age = 0

    for name, info in people.items():
        if info["age"] > oldest_age:
            oldest_age = info["age"]
            oldest_name = name

    print("Oldest person:", oldest_name, "-", oldest_age)

    print("People in New York:")
    for name, info in people.items():
        if info["city"] == "New York":
            print(name)

if __name__ == "__main__":
    people = {
        "Alice": {"age": 30, "city": "New York"},
        "Bob": {"age": 25, "city": "Los Angeles"}, 
        "Charlie": {"age": 35, "city": "Chicago"}
    }

    analyze_people(people)