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

def calculate_type_checker(question,valid_ans=("perimeter", "area")):
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

# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            #check that the number is more than zero
            if 50 > response > 0:
               return  response
            else:
                print(error)
        except ValueError:
            print(error)

def number(low, high):
    return random.randint(low, high)

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")

def check_answer(user_answer, correct_answer):
    if abs(user_answer - correct_answer ) < 0.01:
        print("You are correct")
        return True
    else:
        print(f"Yu are wrong, correct answer is {correct_answer}")
        return False


def instructions():
    """Prints instructions"""

    print("""
                        *** Instructions ****
        This is a calculation test. The program will generate questions with different data points, and you can calculate the answers. 
    The program will check your answers to ensure they are correct.
    
            Don't worry, if your answer is wrong, the program will tell you the correct answer.^-^
    """)


# Main routine Starts here

all_scores = []
feedback = ""
choose = 1


shape_list = ["triangle", "square", "rectangle", "xxx"]
game_history = []
random_number1 = number(5, 30)
random_number2 = number(5, 30)
random_number3 = number(1,20)

print("   □△▭!! Welcome to calculation quiz !!□△▭  ")
print()


# ask user if they wang to see the instructions and display
# them if requested
want_instructions =string_checker("Do you want to see instructions? ")

# checks users enter yes (y) or nno (no)
if want_instructions == "yes":
    instructions()


while True:
    selected_graph = string_checker("Which graphic do you want to learn about?", shape_list)
    print("You choose", selected_graph)
    print()
    formula = calculate_type_checker("you want to calculation perimeter or area ?")
    print("You choose", formula)


    if selected_graph == "square":
        user_answer = float(input(f"What is the {formula} of a square that has a side of {random_number1}? "))
        if formula == "perimeter":
            correct_answer = random_number1 * 4
            is_correct = check_answer(user_answer, correct_answer)
            feedback = "correct" if is_correct else "wrong"

        elif formula == "area":
            correct_answer = random_number1 ** 2
            is_correct = check_answer(user_answer, correct_answer)
            feedback = "correct" if is_correct else "wrong"



    elif selected_graph == "triangle":
        if formula == "perimeter":
            user_answer = float(input(f"What is the {formula} of a triangle that has sides {random_number1}, {random_number2}, {random_number3}? "))
            correct_answer = random_number1 + random_number2 + random_number3
            is_correct = check_answer(user_answer, correct_answer)
            feedback = "correct" if is_correct else "wrong"

        elif formula == "area":
            user_answer = float(input(f"What is the {formula} of a triangle with base {random_number1} and height {random_number3}? "))
            correct_answer = (random_number1 * random_number3) / 2
            is_correct = check_answer(user_answer, correct_answer)
            feedback = "correct" if is_correct else "wrong"

    elif selected_graph == "rectangle":
        if formula == "perimeter":
            correct_answer = 2 * (random_number1 + random_number2)
            user_answer = float(input(f"What is the {formula} of a rectangle with width {random_number1} and height {random_number2}? "))
            is_correct = check_answer(user_answer, correct_answer)
            feedback = "correct" if is_correct else "wrong"



        elif formula == "area":
            correct_answer = random_number1 * random_number2
            user_answer = float(input(f"What is the {formula} of a rectangle with width {random_number1} and height {random_number2}? "))

            is_correct = check_answer(user_answer, correct_answer)
            feedback = "correct" if is_correct else "wrong"


            print(feedback)



    # add round result to game history
    history_feedback = f"Round {choose}: You are {feedback}."

    # Generate history item and add it to game_history list...
    history_item = f"Round {choose}: You choose {selected_graph} {formula} and you are {feedback}."
    game_history.append(history_item)


    keep_going = yes_no("Do you want to continue?")
    print()
    if keep_going == "no":
        break

    choose += 1

print()
# check users have played at least one round
# before calculating statistics area
if choose > 0:

    # Display the game history on request
    see_history = yes_no("Do you want to see your game history? ")

    if see_history == "yes":

        for item in game_history:
            print(item)


    print()
    print(" Thank you use the perimeter and area calculation!!! ")





