# EKSTRAOPPGAVER
# uke 35
# 1
name = input("Enter your name: ")
print("Hello", name, "!")

# 2
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
print ("Total:", num1 + num2)

# 3
number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))
average = (number1 + number2) / 2
print("Your average is: ", average)

# 4
temperture = float(input("Temperature: "))
fahrenheit = (temperture * 9 / 5) + 32
print("Temperature in fahrenheit: ", fahrenheit)

# 5
minutes = int(input("Minutes: "))
hours = minutes // 60
minutes_left = minutes % 60
print(hours, " hours and ", minutes_left, " minutes")

# 6
price = float(input("Price: "))
tip = price * 0.15
total = price + tip
print("Your total is: ", total, "kr, included a 15% tip. The price was originally", price, "kr")

# 7
weight = float(input("Weight: "))
height = float(input("Height: "))
bmi = weight / (height * height)
print("Your bmi is: ", bmi)

# 8
radius = float(input("Radius: "))
area = (radius * radius) * 3.14
print("Your area is: ", area)

# 9
work_hours = float(input("Work hours per day: "))
salary_hours = float(input("Salary per hours: "))
weekly_salary = (work_hours * salary_hours) * 7
print("Your weekly salary is: ", weekly_salary)

# 10
original_price = float(input("Original price: "))
discount_percentage = float(input("Discount percentage: "))
percentage = (original_price * discount_percentage) / 100
total = original_price - percentage
print("Your total is: ", total)


# UKE 36
# LEVEL 1
# Task 1
name = input("Enter your name: ")
print("Hello", name, "!")

# Task 2
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print("Total:", num1 + num2)

# Task 3
score1 = float(input("Enter your first score: "))
score2 = float(input("Enter your second score: "))

average = (score1 + score2) / 2
print("Your average is: ", average)

# Task 4
temperture = float(input("Temperature: "))
fahrenheit = (temperture * 9 / 5) + 32

print("Temperature in fahrenheit: ", fahrenheit)

# Task 5
minutes = int(input("Minutes: "))
hours = minutes // 60
minutes_left = minutes % 60
print(hours, " hours and ", minutes_left, " minutes")


# LEVEL 2
# Task 6
number = float(input("Enter your number: "))

if number > 0:
   print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Task 7
integer = int(input("Enter a number: "))

if integer % 2 == 0:
    print("Even")
else:
    print("Odd")

# Task 8
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))
number_3 = int(input("Enter a number: "))

biggest_number = max(number_1, number_2, number_3)

print(f"The biggest number is {biggest_number}")

# Task 9
score = int(input("Enter your score: "))

if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
elif score > 50:
    print("E")
else:
    print("F")

# Task 10
age = int(input("Enter your age: "))

if age <= 12:
    price = "Free"
elif age <= 18:
    price = 100
elif age <= 65:
    price = 150
else:
    price = 100

print("Your price is: ", price, "kr")


# LOOPS
# Task 11
for number in range(1, 21):
    print(number)

# Task 12
for number in range(1, 51):
    if number % 2 == 0:
        print(number)

# Task 13
for number in range(10, 0, -1):
    print(number)

print("Go!")

# Task 14
number = int(input("Enter a number (1-10): "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Task 15
total = 0

for i in range(1, 101):
    total = total + i

print(total)

# Task 16
for i in range(1,6):
    print("*" * i)


# LEVEL 4
# Task 17
for number in range(1,21):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

# Task 18
for i in range(6,1,-1):
    print("*" * i)

# Task 19
secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

print("Correct! You guessed it.")

# Task 20
for i in range(1, 6):
    print(str(i) * i)

# Task 21
pin = "321"
attempts = 0

while attempts < 3:
    enter_pin = input("Enter your pin: ")
    attempts = attempts + 1

    if enter_pin == pin:
        print("Correct!")
        break
    else:
        print("Wrong!")
else:
    print("Blocked!")

# Task 22
while True:
    print("1. Search catalogue")
    print("2. Renew loan")
    print("3. Check fines")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Searching catalogue...")
    elif choice == 2:
        print("Renewing loan...")
    elif choice == 3:
        print("Checking fines...")
    elif choice == 4:
        print("Goodbye!")
        break

# Task 23
positive = 0
negative = 0
zero = 0

for i in range(1, 6):
    number = int(input("Enter a number: "))

    if number > 0:
        positive = positive + 1
    elif number < 0:
        negative = negative + 1
    else:
        zero = zero + 1

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Zero: {zero}")







