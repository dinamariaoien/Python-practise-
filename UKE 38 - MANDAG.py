# UKE 38
# Mandag
# SAMLINGER
students = ["Sara", "Ahmed", "Lin", "Emma", "Noah"]

for student in students:
    print(student)

# lister (ordnet, kan endres)
# tupler (ordnet, kan ikke endres)
# ordbøker/dictionaries (merket med navn i stedet for posisjon).


# Opprette og indeksere lister
fruits = ["apple", "banana", "cherry", "mango"]
print(fruits)

print(fruits[0])   # apple
print(fruits[2])   # cherry

print(fruits[-1])   # mango  (det siste elementet)
print(fruits[-2])   # cherry (det nest siste elementet)

playlist = ["Baby", "One Less Lonely Gril", "OMW", "Stay Ready"]
print(playlist)

print(playlist[0])
print(playlist[1])
print(playlist[-1])
print(playlist[3])


# SLICING — Hente flere elementer samtidig
fruits = ["apple", "banana", "cherry", "mango", "orange"]

print(fruits[1:3])    # ['banana', 'cherry'] (indeks 1 til, men ikke inkludert, 3)
print(fruits[:2])     # ['apple', 'banana'] (fra starten)
print(fruits[2:])     # ['cherry', 'mango', 'orange'] (til slutten)
print(fruits[:])      # En full kopi av hele listen


# Gå gjennom en liste med en løkke
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):    # Hvis du trenger indeksen i tillegg til verdien, bruker du enumerate():
    print(index, fruit)

# 0 apple
# 1 banana
# 2 cherry
# ...

for index, playlist in enumerate(playlist):
    print(index, playlist)


# NYTTIGE LISTEMETODER
# Legge til elementer
shopping_list = ["milk", "eggs"]

shopping_list.append("bread")         # Legger til på slutten
print(shopping_list)                   # ['milk', 'eggs', 'bread']

shopping_list.insert(0, "coffee")     # Setter inn på en bestemt posisjon
print(shopping_list)                   # ['coffee', 'milk', 'eggs', 'bread']


# Fjerne elementer
shopping_list.remove("eggs")    # Fjerner basert på VERDI
print(shopping_list)             # ['coffee', 'milk', 'bread']

last_item = shopping_list.pop()  # Fjerner og RETURNERER det siste elementet
print(last_item)                  # bread
print(shopping_list)              # ['coffee', 'milk']


# Sortering og andre nyttige verktøy
numbers = [4, 1, 8, 3]

numbers.sort()                   # Sorterer listen (endrer den originale listen)
print(numbers)                    # [1, 3, 4, 8]

numbers.sort(reverse=True)
print(numbers)                    # [8, 4, 3, 1]

print(len(numbers))               # 4 (hvor mange elementer)
print(9 in numbers)               # False (sjekker om 9 finnes i listen)
print(4 in numbers)               # True

# Try yourself
tasks = ["Do homework", "Clean room", "Go to the gym"]

print(tasks)

tasks.append("Buy groceries")
print(tasks)

tasks.remove("Clean room")
print(tasks)


# TUPLE
# En tuple ser ut og fungerer nesten akkurat som en liste, men skrives med vanlige parenteser ( )
# og når den først er opprettet, kan den ikke endres.
coordinates = (59.9139, 10.7522)   # Breddegrad og lengdegrad for Oslo

print(coordinates[0])   # 59.9139

# coordinates[0] = 60.0   # TypeError! Tupler kan ikke endres


# DICTIONARIES - Slå opp ting etter navn
student = {
    "name": "Sara",
    "age": 22,
    "city": "Oslo"
}

print(student["name"])   # Sara
print(student["age"])    # 22

# Legge til, oppdatere og fjerne verdier
student["email"] = "sara@example.com"   # Legger til en ny key
student["age"] = 23                     # Oppdaterer en eksisterende key
print(student)

del student["city"]     # Fjerner en key fullstendig
print(student)

# Gå gjennom en dictionary med en løkke
for key in student:
    print(key, "-", student[key])
# Eller mer direkte:
for key, value in student.items():
    print(key, "-", value)


# Case Study 1 – Shopping Cart Total (List)
# An online store keeps prices in a list and calculates the total with a loop.
cart_prices = [199, 49.90, 320, 15]

total = 0
for price in cart_prices:
    total = total + price

print(f"Total: {total} NOK")   # Total: 583.9 NOK


# Case Study 2 – Student Contact Card (Dictionary)
# A school's digital roster stores each student's details as a dictionary, making lookups instant.
student = {
    "name": "Ahmed",
    "grade": "10th",
    "attendance": 94
}

if student["attendance"] >= 90:
    print(f"{student['name']} has excellent attendance.")
else:
    print(f"{student['name']} needs an attendance check-in.")


# Case Study 3 – RGB Colour Values (Tuple)
# A design tool represents a colour as a fixed set of three numbers that should never accidentally change.
brand_color = (0, 122, 255)   # A shade of blue

red, green, blue = brand_color   # Unpacking a tuple into variables
print(f"R:{red} G:{green} B:{blue}")
# Bonus: This is called tuple unpacking — a very common Python pattern for pulling a tuple's values into separate, clearly-named variables in one line.


# Case Study 4 – Inventory Stock Checker (List + Loop)
# A small warehouse system checks which products are running low on stock.
stock_levels = [45, 3, 120, 8, 0]
product_names = ["Notebook", "Stapler", "Pen", "Folder", "Eraser"]

for i in range(len(stock_levels)):
    if stock_levels[i] < 10:
        print(f"LOW STOCK: {product_names[i]} ({stock_levels[i]} left)")
# Note: This example uses two related lists together, matched up by index. You'll see an even cleaner way to connect this kind of data (using dictionaries or lists of dictionaries) as you progress — but this pattern is a perfectly good starting point.


# Case Study 5 – Restaurant Menu (List of Dictionaries)
# Combining everything from today: a list holding several dictionaries, each representing one menu item.
menu = [
    {"name": "Margherita Pizza", "price": 145},
    {"name": "Caesar Salad", "price": 110},
    {"name": "Spaghetti Bolognese", "price": 165}
]

for item in menu:
    print(f"{item['name']} - {item['price']} NOK")


# Try It Yourself
# EXERCISE 1 · EASY
# Favourite Movies List
movies = ["Shutter Island", "The Godfather", "Spiderman", "Avatar", "Interstellar"]

print(f"You have {len(movies)} favourite movies.")
print(f"First: {movies[0]}")
print(f"Last: {movies[-1]}")

# EXERCISE 2 · EASY
# Sum of a List
daily_steps = [10000, 17000, 4500, 9000, 8800, 23000, 6780]

total_steps = 0
for steps in daily_steps:
    total_steps = total_steps + steps

print(f"Total steps this week: {total_steps}")

# Bonus: Python also has a built-in sum() function
print(f"Same result with sum(): {sum(daily_steps)}")

# EXERCISE 3 · MEDIUM
# To-Do List Manager
tasks = []

tasks.append("Buy groceries")
tasks.append("Finish homework")
tasks.append("Call the dentist")
print("Tasks:", tasks)

tasks.remove("Finish homework")
print("After completing a task:", tasks)

# EXERCISE 4 · MEDIUM
# Contact Card
contact = {
    "name": "Lin",
    "phone": "555-0134",
    "favorite": False
}

print(f"{contact['name']}'s number is {contact['phone']}. Favorite: {contact['favorite']}")

contact["favorite"] = True
print(f"Updated favorite status: {contact['favorite']}")

# EXERCISE 5 · MEDIUM-HARD
# Find the Highest Score
scores = [78, 92, 65, 88, 95, 71]

highest = scores[0]
for score in scores:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")

# Bonus: Python's built-in shortcut
print(f"Same result with max(): {max(scores)}")

# EXERCISE 6 · HARD
# Product Catalogue (List of Dictionaries)
products = [
    {"name": "Notebook", "price": 45},
    {"name": "Backpack", "price": 350},
    {"name": "Pen Set", "price": 60},
    {"name": "Desk Lamp", "price": 120}
]

for product in products:
    line = f"{product['name']} - {product['price']} NOK"
    if product["price"] < 100:
        line = line + " (Budget Pick!)"
    print(line)


# END-OF-LESSON CHALLENGE
# Build a Simple Class Grade Book
students = [
    {"name": "Sara", "grade": 92},
    {"name": "Ahmed", "grade": 58},
    {"name": "Lin", "grade": 76},
    {"name": "Emma", "grade": 84},
    {"name": "Noah", "grade": 45}
]


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


total = 0
highest_student = students[0]
needs_support = []

for student in students:
    letter = get_letter_grade(student["grade"])
    print(f"{student['name']}: {student['grade']} ({letter})")

    total = total + student["grade"]

    if student["grade"] > highest_student["grade"]:
        highest_student = student

    if student["grade"] < 60:
        needs_support.append(student["name"])

average = total / len(students)

print(f"\nClass average: {average:.1f}")
print(f"Top student: {highest_student['name']} ({highest_student['grade']})")
print(f"Needs support: {needs_support}")