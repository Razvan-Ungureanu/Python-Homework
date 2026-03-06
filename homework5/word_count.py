with open("story.txt", "r") as file:
    content = file.read()

words = content.split()

word_count = len(words)

print("Word count:", word_count)