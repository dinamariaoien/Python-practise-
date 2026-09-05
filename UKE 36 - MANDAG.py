# UKE 36
# MANDAG
# indexing
name = "Python"
print(name[
          0])  # 'P'  (first character, index 0)
print(name[
          -1])  # 'n'  (last character, index -1)

# slicing sequence[start:stop:step]
word = "Programming"
print(word[
          0:3])  # 'Pro'   — characters at index 0, 1, 2
print(word[
          :4])  # 'Prog'  — from the start up to (not including) index 4
print(word[
          4:])  # 'ramming' — from index 4 to the end
print(word[
          -3:])  # 'ing'   — the last 3 characters
print(word[
          0:6:2])  # 'Pga'   — every 2nd character from index 0 to 6

numbers = [10, 20, 30, 40, 50]
print(numbers[
          1:3])  # [20, 30]

# reversing
# word[::-1] and reversed() both give you a reversed copy — the original is unchanged.
# list.reverse() is the odd one out: it changes the original list itself and returns None.
word = "Python"
print(word[
          ::-1])  # 'nohtyP'  — negative step walks backwards

numbers = [1, 2, 3, 4, 5]
print(list(reversed(
    numbers)))  # [5, 4, 3, 2, 1] — reversed() works on any sequence

numbers.reverse()  # reverses the list in place, no new list created
print(
    numbers)  # [5, 4, 3, 2, 1]

# Palindrome - same word both ways RADAR ex.
text = input(
    "Enter a word: ").lower()  # . lower Gjør alle bokstavene i teksten om til små bokstaver.
if text == text[::-1]:
    print("That's a palindrome!")
else:
    print("Not a palindrome.")

# Conditions & Decision Making
# Boolean Values
print(10 > 5)
print(10 < 5)

is_raining = True
print(is_raining)
print(type(
    is_raining))  # <class 'bool'>

# Comparison Operators
# ==	Equal to	                age == 18
# !=	Not equal to	            age != 18
# >	    Greater than	            age > 18
# <	    Less than	                age < 18
# >=	Greater than or equal to	age >= 18
# <=	Less than or equal to	    age <= 18

# Chained Comparisons
age = 20
print(
    18 <= age <= 65)  # True — same as: 18 <= age and age <= 65

# if and else
age = 20
if age >= 18:
    print("You are an adult.")

age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

# Multiple Decisions
# We can use elif, which means "else if"
temperature = 15
if temperature >= 25:
    print("It is warm.")
elif temperature >= 15:
    print("It is mild.")
else:
    print("It is cold.")

# Nested if Statements
# An if statement can contain another if statement inside it.
# it's useful when a second decision only makes sense after the first one is already true.
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Please show your ID.")
else:
    print("You must be 18 or older.")

# Conditional Expressions (One-Line if)
# For very simple decisions, Python offers a compact way to write if/else on a single line
# ternary expression
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# Conditions with User Input
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

order_total = float(input("Enter order total: "))
if order_total >= 500:
    print("You get free delivery!")
else:
    print("Delivery fee will be added.")

# Combining Conditions
# Sometimes one comparison is not enough
# Python provides logical operators that allow us to combine conditions.

# and	Both conditions must be true.
# or	At least one condition must be true.
# not	Reverses a Boolean value.

age = 22
has_ticket = True
if age >= 18 and has_ticket:
    print("Entry allowed.")

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It is the weekend.")

logged_in = False
if not logged_in:
    print("Please log in.")

# Combining Several Operators & Operator Precedence
# You can combine and, or and not in the same condition.
age = 20
has_ticket = True
is_vip = False
if (age >= 18 and has_ticket) or is_vip:
    print("Entry allowed.")

# Instead of writing several or comparisons against the same variable, Python lets you check membership in a list directly:
day = "Saturday"
if day in ["Saturday",
           "Sunday"]:  # Lists ([ ]), "is this value one of several options?"
    print("It is the weekend.")

# Case Study 1 – Login System
correct_username = "admin"
correct_password = "python123"

entered_username = input("Username: ")
entered_password = input("Password: ")

if entered_username == correct_username and entered_password == correct_password:
    print("Login successful.")
else:
    print("Login failed.")

# Case Study 2 – Shopping Cart with Discount Tiers
order_total = float(input("Enter order total (NOK): "))

if order_total >= 2000:
    discount = 0.15
elif order_total >= 1000:
    discount = 0.10
elif order_total >= 500:
    discount = 0.05
else:
    discount = 0.0

final_price = order_total - (order_total * discount)
print(f"Discount: {discount * 100}%")
print(f"Final price: {final_price} NOK")
# f gjør at Python skjønner at {} skal behandles spesielt,
# og inni {} kan du enten sette inn en variabel eller et regnestykke.


# Case Study 3 – ATM Withdrawal
balance = 2000
withdrawal = int(input("Enter withdrawal amount: "))

if withdrawal % 100 != 0:  # % finner resten etter divisjon. != betyr "ikke lik"
    print("Amount must be a multiple of 100.")
elif withdrawal > balance:
    print("Insufficient funds.")
else:
    balance = balance - withdrawal
    print(f"Withdrawal approved. New balance: {balance} NOK")

# 500 % 100 gir 0 fordi 500 går opp i 100 uten noe til overs.
# 550 % 100 gir 50 fordi 550 = 5 × 100 + 50

# if withdrawal % 100 != 0 → sjekker om beløpet ikke er et helt hundretall.
# elif withdrawal > balance → sjekker om uttaket er større enn saldoen.
# else → hvis begge sjekkene over er OK, blir uttaket godkjent og beløpet trekkes fra saldoen.
# f"...{balance}..." → setter den nye verdien av balance inn i teksten som skrives ut.


# Case Study 4 – Car Insurance Premium
age = int(input("Enter your age: "))
years_driving = int(input("Years of driving experience: "))
if age < 25 and years_driving < 2:
    print("High risk: premium is 8000 NOK/year.")
elif age < 25 or years_driving < 2:
    print("Medium risk: premium is 5000 NOK/year.")
else:
    print("Standard risk: premium is 3000 NOK/year.")

# Case Study 5 – Traffic Light Simulation
light = input("Enter light colour (red/yellow/green): ")
if light == "red":
    print("Stop.")
elif light == "yellow":
    print("Slow down.")
elif light == "green":
    print("Go.")
else:
    print("Invalid colour.")

# ØVE
# Task 1
number = float(input("Enter a number: "))
if number > 0:
    print("positive")
else:
    print("negative")

# Task 2
integer = float(input("Enter a integer: "))
if integer % 2 == 0:
    print("Even")
else:
    print("Odd")

# Task 3
score = int(input("Enter a score (0-100): "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"
print(f"Your grade is {grade}")

# Task 4
correct_username = "admin"
correct_password = "python123"

entered_username = input("Username: ")
entered_password = input("Password: ")

if entered_username == correct_username and entered_password == correct_password:
    print("Login successful.")
else:
    print("Login failed.")

# Task 5
your_weight = float(input("Enter your weight: "))
your_height = float(input("Enter your height: "))

bmi = your_weight / (your_height ** 100)

if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal"
elif bmi < 30:
    category = "overweight"
else:
    category = "obese"

print(f"Your bmi is {bmi:.1f} ({category})")

# Task 6
age = int(input("Enter your age: "))
rating = int(input("Enter the movie's age rating: "))
with_parent = input("Do you have a parent with you? (yes/no): ").lower() == "yes"

if age < rating and not with_parent:
    print("Not allowed.")
else:
    print("Allowed.")

# End of lesson challenge 1
user_age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no").lower() == "yes"

if user_age < 6:
    ticket_price = 0
elif user_age <= 17:
    ticket_price = 80
elif user_age <= 66:
    ticket_price = 120
    if student:
        ticket_price -= 20
else:
    ticket_price = 80

print(f"Your ticket price is {ticket_price} kr")

# End of lesson challenge 2
bill_amount = float(input("Enter your billing amount: "))
people_eating = int(input("How many people splitting the bill?: "))

if people_eating == 0:
    print("ERROR")
else:
    tip = input("Would you like to add a 10% tip? (yes/no): ").lower() == "yes"
    if tip:
        bill_amount = bill_amount * 1.10

    per_person = bill_amount / people_eating
    print("fEach person will pay: {per_person:.2f} kr")

    if per_person > 300:
        print("That's a lot per person, maybe order fewer dishes next time.")

