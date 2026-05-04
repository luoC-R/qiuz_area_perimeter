import random

def number(low, high):
    return random.randint(low, high)

random_number1 = number(1, 30)
random_number2 = number(1, 20)
print(f"What is the perimeter of a rectangle that has a width of {random_number1} and a height of {random_number2}? ")

