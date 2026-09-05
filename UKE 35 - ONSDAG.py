# ONSDAG uke 35
# STORING INFORMATION
name = "Sara"
age = 20
city = "oslo"

print(name)
print(age)
print(city)

restaurant = "Peppes Pizza"
order = "Margherita"
price = 189
delivery_time = 25
print("Your", order, "from", restaurant, "arrives in", delivery_time, "minutes.")

# Task 1
movie_title = "Seven"
ticket_price = 220
rating = 4
print("You can watch", movie_title, "at Ringen Kino for", ticket_price, "kr and it's rated", rating,
      "stars by Rotten Tomato.")

# Task 2
name = "Dina"
age = 24
hobby = "cycling"
print("My name is", name, ".", "I am", age, "years old, and my hobby is", hobby, ".")

# DIFFERENT TYPES OF DATA
student_name = "Kasper"  # str
student_age = 18  # int
average_grade = 4.5  # float
has_passed = True  # bool
print(type(
    student_age))  # <class 'int'>

# Task 1
caption = "Slay"
likes = 300
avg_watch_time = 3.6
is_verified = False
print(type(caption))
print(type(likes))
print(type(avg_watch_time))
print(type(is_verified))

# USER INPUT
name = input("What is your name? ")
print("Hello", name, "!")

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Welcome back!")
else:
    print("Wrong username or password!")

# Task 1
team = input("What is your favourite team? ")
print("You support", team, "!", "Nice choice!")

# Task 2
city = input("Which city are you in? ")
favourite_food = input("What is your favourite food? ")
print("You live in", city, "and your favourite food is", favourite_food, ".")

# TYPE CONVERSATION
age = int(input("What is your age? "))
print("Next year you will be", age + 1)

# Task 1
current_year = int(input("What is the current year? "))
birth_year = int(input("Which year were you born in? "))
print("You are", current_year - birth_year, "years old.")

# Task 2
temperature = float(input("What is the temperature in celsius? "))
print("The temperature would be", temperature + 1, "if it was 1 degree warmer.")

# CLACULATE - OPERATORS
# Task 1
number1 = int(input("Give a number: "))
number2 = int(input("Give another number: "))
sum = number1 + number2
difference = number1 - number2
product = number1 * number2
print("The sum is", sum)
print("The difference is", difference)
print("The product is", product)

# Task 2
width = float(input("What is the width? "))
height = float(input("What is the height? "))
area = width * height
print("The area is", area)