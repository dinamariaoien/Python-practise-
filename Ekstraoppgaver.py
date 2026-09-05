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







