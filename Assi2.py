with open("sample.txt", "r") as file:
    lines = file.readlines()

    print("Lines:", lines)
    print("Total lines:", len(lines))

    if len(lines) >= 2:
        print("2nd line:", lines[1])
    else:
        print("Second line does not exist")