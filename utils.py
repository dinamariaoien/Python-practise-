# FREDAG uke 37
# Task 11
import random
import datetime

def is_even(number):
    """Return True if the number is even, otherwise False."""
    return number % 2 == 0

def random_number():
    """Return a random number between 1 and 100."""
    return random.randint(1, 100)

def todays_date():
    """Return today's date."""
    return datetime.date.today()