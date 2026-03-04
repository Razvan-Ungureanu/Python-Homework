def analyze_word(word):
    vowels = "aeiou"
    vowel_count = 0

    for char in word.lower():
        if char in vowels:
            vowel_count += 1

    length = len(word)
    uppercase_word = word.upper()

    print("Length:", length)
    print("Vowels:", vowel_count)
    print("Uppercase:", uppercase_word)

if __name__ == "__main__":
    analyze_word("Python")