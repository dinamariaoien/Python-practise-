with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(lines)

with open("highscores.txt", "w") as file:
    file.write("100\n")
    file.write("85\n")
    file.write("70\n")

with open("highscores.txt", "a") as file:
    file.write("60\n")