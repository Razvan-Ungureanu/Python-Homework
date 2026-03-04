def most_frequent_word(text):
    words = text.split()
    word_count = {}

    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    
    max_word = None
    max_count = 0

    for word in word_count:
        if(word_count[word] > max_count):
            max_count = word_count[word]
            max_word = word

    print("Most frequent word:", max_word)
    print("Count:", max_count)

def invert_dictionary(data):
    new_dict = {}

    for name, age in data.items():
        new_dict[age] = name

    return new_dict

if __name__ == "__main__":
    text = "apple banana apple orange banana apple"
    most_frequent_word(text)

    people = {
        "Ana": 25,
        "Ion": 30,
        "Maria": 28
    }

    print(invert_dictionary(people))