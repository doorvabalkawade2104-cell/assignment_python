with open("sample.txt", "r") as f:
    content = f.read()

count = 0

for ch in content.lower():
    if ch in "aeiou":
        count += 1

print("Total vowels:", count)