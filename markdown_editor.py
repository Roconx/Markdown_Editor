a = ""
saved = ""
running = True
while running:
    a = input("Choose a formatter: ")
    if a == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line \nSpecial commands: !help !done")
    elif a == "!done":
        with open("output.md", "w") as f:
            f.write(saved)
        running = False
        continue
    elif a == "plain":
        text = input("Text: ")
        saved = saved + text
        print(saved)
    elif a == "bold":
        text = input("Text: ")
        text = "**" + text + "**"
        saved = saved + text
        print(saved)
    elif a == "italic":
        text = input("Text: ")
        text = "*" + text + "*"
        saved = saved + text
        print(saved)
    elif a == "inline-code":
        text = input("Text: ")
        text = "`" + text + "`"
        saved = saved + text
        print(saved)
    elif a == "link":
        label = input("Label: ")
        url = input("URL: ")
        text = "[" + label + "](" + url + ")"
        saved = saved + text
        print(saved)
    elif a == "header":
        level = int(input("Level: "))
        while not(1 <= level <= 6):
            print("The level should be within the range of 1 to 6")
            level = int(input("Level: "))
        text = input("Text: ")
        text = "#"*level + " " + text
        if saved == "":
            saved = saved + text + "\n"
        else:
            saved = saved + "\n" + text + "\n"
        print(saved)
    elif a == "unordered-list":
        rows = int(input("Number of rows: "))
        while rows < 1:
            print("The number of rows should be greater than zero")
            rows = int(input("Number of rows: "))
        for i in range(1, rows+1):
            saved += "* " + input(f"Row #{i}: ") + "\n"
        print(saved)
    elif a == "ordered-list":
        rows = int(input("Number of rows: "))
        while rows < 1:
            print("The number of rows should be greater than zero")
            rows = int(input("Number of rows: "))
        for i in range(1, rows+1):
            saved += f"{i}. " + input(f"Row #{i}: ") + "\n"
        print(saved)
    elif a == "new-line":
        saved = saved + "\n"
        print(saved)
    else:
        print("Unknown formatting type or command")
