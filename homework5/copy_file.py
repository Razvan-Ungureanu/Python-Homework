with open("source.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as copy:
    copy.write(content)

print("Content copied successfully.")