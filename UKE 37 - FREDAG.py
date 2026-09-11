# Function Basics Review
# Task 1 – Your First Function
def greet():
    print("Welcome to Python!")

greet()


# Task 2 – Add a Parameter
def greet(name):
    print(f"Hi {name}! Welcome to Python!")

greet("Sara")
greet("Alice")
greet("Linn")


# Task 3 – Multiple Parameters
def introduce(name, age, city):
    print(f"My name is {name}, I am {age} years old and I live in {city}.")

introduce("Sara", 25, "Oslo")


# Task 4 – Returning a Value
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
# print displays, return can actually perform a task


# Task 5 – Build a Calculator Function
def multiply(a, b):
    return a * b
answer = multiply(6, 4)
print(answer)

def add(a, b):
    return a + b
result = add(10, 5)
print(result)

def subtract(a, b):
    return a - b
result = subtract(10, 5)
print(result)

def devide(a, b):
    return a / b
result = devide(10, 5)
print(result)


# Task 6 – Functions + Conditions
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

result = check_age(12)
print(result)


def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

result = check_age(18)
print(result)


def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

result = check_age(25)
print(result)


def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

result = check_age(70)
print(result)


# Task 7 – Price Calculator
def calculate_total(price, quantity, discount=0):
    return price * quantity - discount

total = calculate_total(49, 3, 15)
print(f"Total: {total} NOK")


# Task 8 – Shipping Cost Function
def calculate_shipping(order_total, weight_kg):
    if order_total >= 1000:
        return 0
    else:
        return weight_kg * 20

print(f"Shipping cost: {calculate_shipping(666, 35)} NOK")
print(f"Shipping cost: {calculate_shipping(1000, 80)} NOK")
print(f"Shipping cost: {calculate_shipping(350, 60)} NOK")


# Task 9 – Debug the Function
def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average

print(calculate_average(10, 20, 30))