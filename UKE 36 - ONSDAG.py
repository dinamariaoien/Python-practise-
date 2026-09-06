# UKE 36 - ONSDAG
# LOOPS
for number in range(1,6):         # Teller til 5 fra 1-5
    print(number)

for number in range(5):           # Printer "Welcome!" 5 ganger
    print("Welcome!")

for number in range(0,11,2):      # Teller til 10, men printer annenhvert tall
    print(number)                 # Start, stop, step


# Loop patterns
for i in range(6):                # Printer * på linje under hverandre 5 ganger
    print("*")

for i in range(1,8):              # Printer * i et stingende mønster 7 ganger
    print("*" * i)


# Telle baklengs
for number in range(5, 0, -1):
    print(number)

print("Go!")


# Bruke loop-variabelen
for number in range(1, 6):
    square = number * number
    print(number, "squared is", square)


# Nested loops
for row in range(1,6):
    for seat in range(1,4):
        print(f"Row {row}, Seat {seat}")


# For loop over tekst
name = "Sara"
for letter in name:
    print(letter)


# Practical Example – Savings Calculator
monthly_saving = 100
total = 0

for month in range(1,7):
    total = total + monthly_saving
    print("Month", month, "- Total:", total, "nok")


# While loop
number = 1                         # En while-løkke gjentar kode så lenge en betingelse er True (sann).
while number <= 10:
    print(number)
    number = number + 1


# Practical Example – Password Check
password = ""                                       # En while-løkke er nyttig når vi ikke vet nøyaktig hvor mange
                                                    # forsøk eller repetisjoner som vil være nødvendig.
while password != "python123":
    password = input("Enter your password: ")

print("access granted")


# Condition i loops
for number in range(1,11):

    if number % 2 == 0:
        print("number",number, "is even")
    else:
        print("number",number, "is odd")


# Break
for number in range(1,11):                        # Noen ganger vil man stoppe loopen, før den normalt hadde endt

    if number == 6:
        break
    print(number)


# Continue
for number in range(1,11):                       # Continue hopper over resten av den nåværende repetisjonen og går videre til den neste.

    if number == 6:
        continue
    print(number)


# CASE STUDIES
# Case Study 1 – Grocery Store Checkout
number_of_items = int(input("How many items are you buying? "))
total = 0

for item in range(1, number_of_items + 1):
    price = float(input(f"Enter price for item {item}: "))
    total = total + price

print(f"Total to pay: {total} NOK")


# Case Study 2 – Workout Rep Counter
for rep in range(1, 11):
    print(f"Push-up {rep} - keep going!")

print("Workout complete!")


# Case Study 3 – Bus Arrival Countdown
minutes_until_bus = 5

while minutes_until_bus > 0:
    print(f"Bus arrives in {minutes_until_bus} minute(s).")
    minutes_until_bus = minutes_until_bus - 1

print("The bus has arrived!")


# Case Study 4 – ATM PIN Attempts (while + break + counter)
correct_pin = "4321"
attempts = 0

while attempts < 3:
    entered_pin = input("Enter your pin: ")
    attempts = attempts + 1

    if entered_pin == correct_pin:
        print("Correct!")
        break
    else:
        print("Incorrect. Try again.")

else:
    print("Card blocked")


# Case Study 5 – Elevator Floor Announcer (nested-loop-friendly)
top_floor = 8

for floor in range(1, top_floor + 1):
    if floor == 0:
        print("Ground floor", floor)
    else:
        print(f"Floor {floor}")


# Case Study 6 – Classroom Seating Chart (nested loop)
rows = 3
seats_per_row = 5

for row in range(1, rows + 1):
    for seat in range(1, seats_per_row + 1):
        print(f"Row {row}, Seat {seat}")
    print("---")   # Separator between rows


# ØVE
# Task 1
for number in range(1, 11):
    print(number)

# Task 2
for number in range(2, 21, 2):
    print(number)

# Task 3
num = int(input("Enter a number: "))

for number in range(1,11):
     print(f"{number} x {i} = {number * i}")

# Task 4
items = int(input("How many items are you buying? "))
total = 0

for item in range(1, items + 1):
    price = float(input(f"Enter price for item {item}: "))
    total = total + price
print(f"Total to pay: {total} NOK")

# Task 5
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days:
    for period in range(1, 4):
        print(f"{day} - Period {period}")


# Task 6
secret_number = 17
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

print("Correct! You guessed it.")


# End of lesson challenge
balance = 1000
running = True

while running:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print(f"Your balance is {balance} NOK")

    elif choice == "2":
        amount = float(input("Amount to deposit: "))
        balance = balance + amount
        print(f"New balance: {balance} NOK")

    elif choice == "3":
        amount = float(input("Amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance = balance - amount
            print(f"New balance: {balance} NOK")

    elif choice == "4":
        print("Thank you, goodbye!")
        running = False

    else:
        print("Invalid option, please try again.")