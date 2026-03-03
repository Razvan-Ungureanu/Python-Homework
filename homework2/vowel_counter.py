word = input("Enter a word: ")
count = 0
vowels_found = " "

for char in word:
    if char.lower() in "aeiou":
        count += 1
        vowels_found += char

print("Number of vowels:", count)
print("Vowels found:", vowels_found)