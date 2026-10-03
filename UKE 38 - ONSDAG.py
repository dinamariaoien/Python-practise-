notes = []
notes.append("Buy milk")
print(notes)
# Close the program... "Buy milk" is gone forever.

file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()   # Always close a file when you're done with it


# .read() — the whole file as one string
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()


# .readlines() — a list, one item per line
file = open("notes.txt", "r")
lines = file.readlines()
print(lines)   # ['Buy milk\n', 'Call the dentist\n', 'Finish homework']
file.close()


# Looping directly over the file — one line at a time
file = open("notes.txt", "r")
for line in file:
    print(line.strip())   # .strip() removes the trailing newline
file.close()


# With statement
file = open("notes.txt", "r")
content = file.read()
file.close()   # Easy to forget, or skipped entirely if an error happens above

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
# The file is automatically closed here, even if an error occurred above


# Writing — creates new content, erasing anything old
with open("notes.txt", "w") as file:
    file.write("Buy milk\n")
    file.write("Call the dentist\n")


# Appending — adds to the end, keeping existing content
with open("notes.txt", "a") as file:
    file.write("Finish homework\n")
# The file now has all 3 lines - nothing was erased


# Writing several lines at once
tasks = ["Buy milk\n", "Call the dentist\n", "Finish homework\n"]

with open("notes.txt", "w") as file:
    file.writelines(tasks)


# Character Encoding
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Møte i morgen kl. 14:00 – ta med kaffe ☕\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())


# Processing Data from Files
grades = []

with open("grades.txt", "r", encoding="utf-8") as file:
    for line in file:
        grade = int(line.strip())   # strip() removes the \n, int() converts it
        grades.append(grade)

average = sum(grades) / len(grades)
print(f"Average grade: {average:.1f}")


# 2
contacts = []

with open("contacts.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, phone = line.strip().split(",")
        contacts.append({"name": name, "phone": phone})

for contact in contacts:
    print(f"{contact['name']}: {contact['phone']}")


# Try it now
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


# Case studies
# Personal Diary App
entry = input("What happened today? ")

with open("diary.txt", "a", encoding="utf-8") as file:
    file.write(entry + "\n")

print("Entry saved!")


# Log File Error Counter
error_count = 0

with open("server_log.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1

print(f"Found {error_count} error(s) in the log.")


# Word Frequency Counter
word_counts = {}

with open("essay.txt", "r", encoding="utf-8") as file:
    text = file.read()
    words = text.lower().split()

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)


# Backup Copy Tool
with open("notes.txt", "r", encoding="utf-8") as original:
    content = original.read()

with open("notes_backup.txt", "w", encoding="utf-8") as backup:
    backup.write(content)

print("Backup created!")


# High Score Table
scores = []

with open("highscores.txt", "r", encoding="utf-8") as file:
    for line in file:
        scores.append(int(line.strip()))

new_score = 850
scores.append(new_score)
scores.sort(reverse=True)
top_five = scores[:5]

with open("highscores.txt", "w", encoding="utf-8") as file:
    for score in top_five:
        file.write(str(score) + "\n")

print("High score table updated!")


# Try it yourself
# 1 - Save Your Favourite Movies
movies = ["Inception", "The Matrix", "Interstellar", "Arrival"]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(movie + "\n")

print("Movies saved!")


# 2 - Read Them Back
saved_movies = []

with open("movies.txt", "r", encoding="utf-8") as file:
    for line in file:
        saved_movies.append(line.strip())

print(f"Loaded {len(saved_movies)} movies:")
for movie in saved_movies:
    print(f"- {movie}")


# 3 - Simple Diary Entry
entry = input("What happened today? ")

with open("diary.txt", "a", encoding="utf-8") as file:
    file.write(entry + "\n")

print("Entry saved!")


# 4 - Grade Average from a File
grades = []

with open("grades.txt", "r", encoding="utf-8") as file:
    for line in file:
        grades.append(int(line.strip()))

average = sum(grades) / len(grades)
print(f"Average grade: {average:.1f}")


# 5 - Contact List Loader
contacts = []

with open("contacts.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, phone = line.strip().split(",")
        contacts.append({"name": name, "phone": phone})

for contact in contacts:
    print(f"{contact['name']}: {contact['phone']}")


# 6 - Word Counter
with open("article.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()
print(f"Word count: {len(words)}")


# End of lesson challenge
import os

FILENAME = "my_notes.txt"
running = True

while running:
    print("\n1. Add a note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        note = input("Enter your note: ")
        with open(FILENAME, "a", encoding="utf-8") as file:
            file.write(note + "\n")
        print("Note saved!")

    elif choice == "2":
        if not os.path.exists(FILENAME):
            print("No notes yet.")
        else:
            with open(FILENAME, "r", encoding="utf-8") as file:
                notes = file.readlines()

            if len(notes) == 0:
                print("No notes yet.")
            else:
                for index, note in enumerate(notes, start=1):
                    print(f"{index}. {note.strip()}")

    elif choice == "3":
        with open(FILENAME, "w", encoding="utf-8") as file:
            pass  # Opening in "w" mode and writing nothing clears the file
        print("All notes deleted.")

    elif choice == "4":
        print("Goodbye!")
        running = False

    else:
        print("Invalid option, please try again.")
