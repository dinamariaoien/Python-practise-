# FREDAG uke 36
# LEVEL 1
# Task 1
age = int(input("What is your age? "))

if age <= 13:
    print("Child")
elif age <= 17:
    print("Teen")
else:
    print("Adult")

# Task 2
for number in range(1, 21):
    print(number)

# Task 3
for number in range(1, 21):

    if number % 2 == 0:
        print(number, "Even")

# eller
for number in range(2, 21, 2):
    print(number)


# LEVEL 2
# Task 1
number = int(input("Please enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Task 2
for i in range(1,6):
    number = float(input(f"Enter number {i}: "))

    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
        print("zero")

# Task 3
total = 0

for i in range(1,6):
    number = float(input(f"Enter number {i}: "))
    total = number + total

average = total / 5

print(f"total km for the week: {total}. And average km per day: {average}.")


# LEVEL 3
# Task 1
correct_username = "admin"
correct_password = "python12"

attempts = 0
logged_in = False

while attempts < 3 and not logged_in:
    entered_username = input("Please enter your username: ")
    entered_password = input("Please enter your password: ")
    attempts = attempts + 1

    if entered_username == correct_username and entered_password == correct_password:
        logged_in = True
        print("Logged in")
    else:
        print("Incorrect username or password")

if not logged_in:
    print("Account locked")

# Task 2
order = float(input("Please enter your order value: "))

if order < 500:
    total_price = order
elif order < 999:
    total_price = order - (order * 0.10)
else:
    total_price = order - (order) * 0.2

print(f"Your total price is {total_price} kr.")

# Fasit
order_total = float(input("Enter order total (NOK): "))

if order_total < 500:
    discount_rate = 0
elif order_total < 1000:
    discount_rate = 0.10
else:
    discount_rate = 0.20

discount_amount = order_total * discount_rate
final_price = order_total - discount_amount

print(f"Original price: {order_total} NOK")
print(f"Discount: {discount_amount} NOK")
print(f"Final price: {final_price} NOK")

# Task 3
secret_number = 67
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")

print("Correct!")

# Fiksa kode
number = 1

while number <= 5:
    print(number)
    number = number + 1

# Ekstra - fikk ikke til
balance = 1000
transaction_count = 0
running = True

while running:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print(f"Your balance is {balance} NOK")

    elif choice == "2":
        amount = float(input("Amount to deposit: "))
        balance = balance + amount
        transaction_count = transaction_count + 1
        print(f"New balance: {balance} NOK")

    elif choice == "3":
        amount = float(input("Amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance = balance - amount
            transaction_count = transaction_count + 1
            print(f"New balance: {balance} NOK")

    elif choice == "4":
        print(f"You made {transaction_count} transaction(s). Goodbye!")
        running = False

    else:
        print("Invalid option, please try again.")