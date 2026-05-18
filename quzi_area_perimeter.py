import random

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

   error = f"Please enter s valid option from the following list: {valid_ans}"

   while True:

       # Get user response and make sure it's lowercase
       user_response = input(question).lower()

       for item in valid_ans:
           # check if the user response is a word in the list
           if item == user_response:
               return item

           # check if the user response is the same as
           # the first letter of an item in the list
           elif user_response == item[0]:
               return item

       # print error if user does not enter something that is valid
       print(error)
       print()


def number(low, high):
    return random.randint(low, high)


def check_answer(user_answer, correct_answer):
    if abs(user_answer - correct_answer ) < 0.01:
        print("You are correct")
        return True
    else:
        print(f"You are wrong, correct answer is {correct_answer}")
        return False


def instructions():
    """Prints instructions"""

    print("""
                        *** Instructions ****
        This is a calculation test. The program will generate questions with different data points, and you can calculate the answers. 
    The program will check your answers to ensure they are correct.
    
            Don't worry, if your answer is wrong, the program will tell you the correct answer.^-^
    """)

def get_number_input(prompt):
    """Gets a valid number from user, keeps asking until they enter one."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

# Main routine Starts here

MIN_LARGE = 5
MAX_LARGE = 30
MIN_SMALL = 1
MAX_SMALL = 20
choose = 1

formula_list = ["perimeter", "area"]
shape_list = ["triangle", "square", "rectangle",]
quiz_history = []



print("   □△▭!! Welcome to calculation quiz !!□△▭  ")
print()


# ask user if they wang to see the instructions and display
# them if requested
want_instructions =string_checker("Do you want to see instructions? ")

# checks users enter yes (y) or nno (no)
if want_instructions == "yes":
    instructions()



while True:
    num1 = number(MIN_LARGE, MAX_LARGE)
    num2 = number(MIN_LARGE, MAX_LARGE)
    num3 = number(MIN_SMALL, MAX_SMALL)
    selected_shape = string_checker("Which shape do you want to learn about?", shape_list)
    print("You choose", selected_shape)
    print()
    formula = string_checker("you want to calculation perimeter or area ?", formula_list)
    print("You choose", formula)

    # Generate question and calculate correct answer based on shape

    if selected_shape == "square":
        user_answer =  get_number_input(f"What is the {formula} of a square that has a side of {num1}? ")
        if formula == "perimeter":
            correct_answer = num1 * 4
        else:
            correct_answer = num1 ** 2
        detail = f"side={num1}"

    elif selected_shape == "triangle":
        if formula == "perimeter":
            user_answer =  get_number_input(f"What is the {formula} of a triangle that has sides base{num1}, side{num2}, side{num3}?")
            correct_answer = num1 + num2 + num3
        else:
            user_answer =  get_number_input(f"What is the {formula} of a triangle with base {num1} and height {num3}?")
            correct_answer = num1 * num3 / 2
        detail = f"sides={num1},{num2},{num3}"

    elif selected_shape == "rectangle":
        user_answer =  get_number_input(f"What is the {formula} of a rectangle with width {num1} and height {num2}?")
        if formula == "perimeter":
            correct_answer = 2 * (num1 + num2)
        else:
            correct_answer = num1 * num2
        detail = f"width={num1}, height={num2}"

    # Validate user answer (works for all shapes since variables are set above)
    is_correct = check_answer(user_answer, correct_answer)


    # Generate history item and add it to game_history list...
    if is_correct:
        history_item = f"Round {choose}: {selected_shape} {formula}, {detail} = {correct_answer} <correct>"
    else:
        history_item = f"Round {choose}: {selected_shape} {formula}, {detail} = {correct_answer} <wrong, your answer was {user_answer}>"

    quiz_history.append(history_item)

    # ask user if they want break/continue
    keep_going = string_checker("Do you want to continue?")
    print()
    if keep_going == "no":
        break

    # keep the round number can not only same number
    choose += 1

print()
# check users have played at least one round
# before calculating statistics area
if choose > 0:

    # Display the game history on request
    see_history = string_checker("Do you want to see your game history? ")

    # check user if they want to see history or not
    if see_history == "yes":

        for item in quiz_history:
            print(item)


    print()
    print(" Thank you use the perimeter and area quiz!!! ")





