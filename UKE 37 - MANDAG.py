# FUNCTIONS
import numbers

from Ekstraoppgaver import choice


def greet(name):
    print("Hello,", (name), "!")
    print("Welcome!")

greet("Sara")
greet("Ahmed")
greet("Lin")

# defining function
# nothing happens until you call it, we have only defined the function
def morning_routine():
    print("Wake up")
    print("Brush teeth")
    print("Eat breakfast")

# calling a function
def morning_routine():
    print("Wake up")
    print("Brush teeth")
    print("Eat breakfast")
morning_routine()   # now it shows up - because you have called it

# parameter and arguments
def lucky_number():
    print("8")
lucky_number()

def lucky_number(number):
    print("My favourite number is", number)
lucky_number(8)

def lucky_number(number):
    print(f"My favourite number is {number}")
lucky_number(8)



def order_pizza(topping):
    print(f"One pizza with {topping} coming up!")

order_pizza("peperoni")
order_pizza("cheese")
order_pizza("mushrooms")
order_pizza("meat")



def coffee(type):
    print(f"Here is your {type}!")

coffee("americano")
coffee("cappuccino")
coffee("hot chocolate")
coffee("moccha")



# Print vs. return
# just displays - gives nothing back
def add_print(a, b):
    print(a + b)

result = add_print(1, 2)  # prints "7"
print(result)                   # prints None



# return
# sends the value back so we can use it
def add_return(a, b):
    return a + b

result = add_return(1, 2)    # Nothing printed yet
print(result)                      # Prints "3"

total = add_return(1, 2) + add_return(2, 3)
print(total)



def add_return(a, b):
    return a + b

result = add_return(6, 3) * add_return(1, 9)
print(result)



# default parameter values
def greet(name, greeting="Welcome"):
    print(f"{greeting}, {name}!")

greet("Sara")
greet("Ahmed", "Good morning")

# 2
def greet(name = "Sara", greeting="Welcome"):
    print(f"{greeting}, {name}!")

greet()

# 3
def greet(name = "Sara", greeting="Welcome"):
    print(f"{greeting}, {name}!")

greet("Ahmed")

# 4
def greet(name = "Sara", greeting="Welcome"):
    print(f"{greeting}, {name}!")

greet("Ahmed", "Hello")

# 5
def order_coffee(size = "medium"):
    print(f"One {size} coffee please!")

order_coffee()
order_coffee("large")

# 6
def order_coffee(size = "medium", milk = True):
    print(f"One {size} coffee, with milk {milk} please!")

order_coffee()
order_coffee("large", False)


# Multiple parameters and multiple return values
def calculate_price(quantity, unit_price):
    return quantity * unit_price

total = calculate_price(3, 100)
print(total)

# 2
def min_and_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_and_max([6, 7, 3, 8, 1])
print(f"lowest: {lowest}, highest: {highest}")

# 3
def profile(name, age, address):
    print(f"The name is {name} and you are {age} years old. You live in {address}")

profile("Sara", 20, "Oslo")


# positional vs keyword arguments
# by default, arguments are matched to parameters by their position (order)
def describe_pet(name, animal_type):
    print(f"{name} is a {animal_type}.")

describe_pet("Max", "dog")
describe_pet(animal_type = "dog", name = "Luna")

#2
def order_coffee(size = "medium", milk = True):
    print(f"One {size} coffee, with milk {milk} please!")

order_coffee(milk = False, size = "small")


# Variable scope: local vs global
tax_rate = 0.25   # global

def calculate_total(price):
    return price + (price * tax_rate)

print(calculate_total(100))

def calculate_total():
    total = 100   # local - only exists inside this function
    return total

calculate_total()
print(total)


# CASE STUDIES
# Case Study 1 – Shopping Cart Total
def calculate_order_total(price, quantity, tax_rate=0.25):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax

total = calculate_order_total(199, 2)
print(f"Total: {total} NOK")   # Total: 497.5 NOK


# Case Study 2 – BMI Calculator as a Function
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

my_bmi = calculate_bmi(70, 1.75)
print(f"BMI: {my_bmi:.1f} ({bmi_category(my_bmi)})")


# Case Study 3 – Grade Checker as a Function
def get_grade(score):
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

students = {"Sara": 95, "Ahmed": 72, "Lin": 58}

for student, score in students.items():
    print(f"{student}: {get_grade(score)}")


# Case Study 4 – Temperature Converter Toolkit
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(celsius_to_fahrenheit(20))   # 68.0
print(fahrenheit_to_celsius(68))   # 20.0


# Case Study 5 – Password Strength Checker
def check_password_strength(password, min_length=8):
    if len(password) < min_length:
        return False, f"Password must be at least {min_length} characters"

    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False, "Password must contain at least one number"

    return True, "Password is strong"

is_valid, message = check_password_strength("hello123")
print(message)   # Password is strong


# Library late fee calculator
def calculate_fee(days_late, fee_per_day=2, max_fee=50):
    if days_late <= 0:
        return 0

    fee = days_late * fee_per_day

    if fee > max_fee:
        return max_fee

    return fee

def fee_message(days_late):
    fee = calculate_fee(days_late)

    if fee == 0:
        return "No late fee - thank you for returning on time!"

    return f"This book is {days_late} day(s) late. Fee: {fee} NOK"

print(fee_message(0))    # No late fee - thank you for returning on time!
print(fee_message(5))    # This book is 5 day(s) late. Fee: 10 NOK
print(fee_message(40))   # This book is 40 day(s) late. Fee: 50 NOK


# ØVE
# Task 1
def greet(name, greeting="Welcome"):
    print(f"{greeting}, {name}!")

greet("Sara")
greet("Ahmed")
greet("Lin")


# Task 2
def square(number):
    return number ** 2

square(3)


# Task 3
def rectangle_area(width, height):
    return width * height

def describe_rectangle(width, height, unit="cm"):
    area = rectangle_area(width, height)
    return f"The area is {area} {unit}\u00b2"

print(describe_rectangle(4, 5))          # The area is 20 cm²
print(describe_rectangle(4, 5, "m"))     # The area is 20 m²


# Task 4
def is_even(number):
    return number % 2 == 0

for number in range(1, 11):
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


# Task 5
def apply_discount(total):
    if total < 500:
        discount_rate = 0
    elif total < 1000:
        discount_rate = 0.1
    else:
        discount_rate = 0.2

    return total - (total * discount_rate)

order_total = float(input("Enter your order total: "))
final_price = apply_discount(order_total)
print(f"Final price: {final_price} NOK")


# Task 6
def number_stats(numbers):
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for number in numbers:
        if number > 0:
            positive_count = positive_count + 1
        elif number < 0:
            negative_count = negative_count + 1
        else:
            zero_count = zero_count + 1

    return positive_count, negative_count, zero_count

positive_count, negative_count, zero_count = number_stats([4, -2, 0, 7, -9, 0, 3])
print(f"Positive count: {positive_count}")
print(f"Negative count: {negative_count}")
print(f"Zero count: {zero_count}")

# calculator tool
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

running = True

while running:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an operation (1-5): ")

    if choice == "5":
        print("Goodbye!")
        running = False
        continue

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid option, please try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(f"Result: {add(num1, num2)}")
    elif choice == "2":
        print(f"Result: {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Result: {multiply(num1, num2)}")
    elif choice == "4":
        print(f"Result: {divide(num1, num2)}")