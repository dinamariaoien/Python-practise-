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
print("You can watch", movie_title, "at Ringen Kino for", ticket_price, "kr and it's rated", rating, "stars by Rotten Tomato.")

# Task 2
name = "Dina"
age = 24
hobby = "cycling"
print("My name is", name,".", "I am", age, "years old, and my hobby is", hobby,".")


# DIFFERENT TYPES OF DATA
student_name = "Kasper" # str
student_age = 18 # int
average_grade = 4.5 # float
has_passed = True # bool
print(type(student_age)) # <class 'int'>

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
print("Hello", name,"!")

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Welcome back!")
else:
    print("Wrong username or password!")

# Task 1
team = input("What is your favourite team? ")
print("You support", team,"!", "Nice choice!")

# Task 2
city = input("Which city are you in? ")
favourite_food = input("What is your favourite food? ")
print("You live in", city, "and your favourite food is", favourite_food,".")


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


# FREDAG
# BLOCK 1
# Task 1
favorite_song = "Baby"
artist = "Justin Bieber"
print("Now playing:", favorite_song, "by", artist)

# Task 2
friend_1 = "Lisa"
friend_2 = "Mia"
friend_3 = "Leni"
print("1.", friend_1)
print("2.", friend_2)
print("3.", friend_3)
print("1. " + friend_1 + "\n2. " + friend_2 + "\n3. " + friend_3)

# Task 3
item = "Notebook"
quantity = 3
unit_price = 25
print( quantity, "x", item, "=", quantity * unit_price, "kr")

# BLOCK 2
# Task 1
city = "Bergen" #str
temperature = 14.5 #float
print("Weather in", city) # printer hva været er i oppført by
print(temperature, "degrees") # printer hva temperaturen er

# Task 2
item = "Notebook"
quantity = 3
unit_price = 25
# "Notebook" er tekst og må markeres med "", Tall er statiske så det må stå uten "", slik at programet klarer å regne
print( quantity, "x", item, "=", quantity * unit_price, "kr") # * = multiplikasjon

# BLOCK 3
# Task 1
city = "Bergen"
temperature = 14.5
humidity = 75
is_raining = True
print(city, type(city))
print(temperature, type(temperature))
print(humidity, type(humidity))
print(is_raining, type(is_raining))

# Task 2
print(type("100"))
print(type(100))
print(type(100.0))
print(bool, type(True))
print(type("True"))

# Task 3
# kræsjer fordi age er oppført som tekst og ikke et statisk tall

age = 20
print("Next year you will be", age + 1)

# BLOCK 4
# task 1
favourite_movie= input("What is your favourite movie?")
release_year= input("What is the release year?")
print("Your favourite movie is", favourite_movie, "and it was released in", release_year)

# Task 2
animal= input("Give me an animal:")
color= input("Give me a color:")
place= input("Give me a place:")
print("A", color, animal, "in", place, "- cool!")

# Task 3
number_1 = int(input("Give me a number:"))
number_2 = int(input("Give me another number:"))

if number_1 > number_2:
    print("number 1 is bigger than number 2")
else:
    print("number 2 is bigger than number 1")

# BLOCK 5
# Task 1
number_one = int(input("First number: "))
number_two = int(input("Second number: "))
sum = number_one + number_two

# Task 2
price = float(input("What is the price?"))
vat = price * 0.25
total_price = price + vat
print("The total price included 25% VAT is ", total_price)

# BLOCK 6
# Task 1
weight = float(input("Weight in kg: "))
height = float(input("Height in m: "))
bmi = weight / height ** 2
print("Your BMI is", bmi)

# Task 2
total_minutes = int(input("Give me a number of total minutes"))
hours = total_minutes // 60
minutes = total_minutes % 60
print(total_minutes, "minutes is", hours, "hours and", minutes, "minutes.")

# Task 3
rectangle_height = float(input("What is the heighth of this rectangle?"))
rectangle_width = float(input("What is the witdh of this rectangle?"))
area = rectangle_height * rectangle_width
perimeter = (rectangle_height + rectangle_width) * 2
print("The area is", area)
print("The perimeter is", perimeter)

# Task 4
number = int(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print("Square:", square)
print("Cube:", cube)

# BLOCK 7
# Project A
total_amount = float(input("What was the total on the bill?")) # int gjør om tekst til tall
people_splitting = int(input("How many is splitting the bill?"))
sum_each = total_amount / people_splitting # dividerer hele beløpet på antallet
print("Each person owes", sum_each, "kr")

# Project B
score1 = float(input("What is the first score?"))
score2 = float(input("What is the second score?"))
score3 = float(input("What is the third score?"))
average = (score1 + score2 + score3) / 3
print("The average is", average)

# Project C
amount = float(input("Total amount in NOK: "))
usd = amount * 0.095
eur = amount * 0.087
print(amount," kr is", usd, " USD, and", eur, " EUR.")

# Bonus
price = float(input("Price for one pizza: "))
quantity = int(input("Number of pizzas: "))
total = price * quantity

if quantity >= 3:
    total_price = total * 0.85
else:
    total_price = total
print("Total to pay:", round(total, 2), "kr")


# Ekstraoppgaver
print(total_price)





























