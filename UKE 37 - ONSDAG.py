# ONSDAG uke 37
# Modules, Documentation & Simple Git Flow

# gjorde det i en annen mappe - modules_practice


# Case Study 1 – Personal Budget App Split Into Modules
# budget.py
"""Functions for calculating budget totals."""

def total_expenses(expenses):
    """Return the sum of a list of expense amounts."""
    return sum(expenses)

def remaining_budget(income, expenses):
    """Return income minus total expenses."""
    return income - total_expenses(expenses)
# main.py
import budget

my_expenses = [1200, 450, 300, 89]
income = 3500

left_over = budget.remaining_budget(income, my_expenses)
print(f"You have {left_over} NOK left this month.")



# Case Study 2 – Quiz Game Using a Built-in Module
# quiz.py
"""A tiny quiz module for practicing capitals."""
import random

questions = {
    "What is the capital of Norway?": "Oslo",
    "What is the capital of France?": "Paris",
    "What is the capital of Japan?": "Tokyo"
}


def ask_random_question():
    """Pick a random question and check the user's answer."""
    question = random.choice(list(questions.keys()))
    answer = input(question + " ")

    if answer.strip().lower() == questions[question].lower():
        return "Correct!"
    else:
        return f"Wrong! The answer was {questions[question]}"


if __name__ == "__main__":
    print(ask_random_question())



