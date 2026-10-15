with open("sample.txt", "r") as f:
    content = f.read()

words = content.split()

print("Words:", words)
print("Total words:", len(words))
print("Unique words:", set(words))