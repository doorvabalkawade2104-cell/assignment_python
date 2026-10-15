with open("sample.txt", "r") as file:
    content = file.read()

    words = content.split()

    print("Longest word:", max(words, key=len))