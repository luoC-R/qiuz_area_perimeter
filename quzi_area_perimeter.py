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

feedback = ""
choose = 1

formula_list = ["perimeter", "area"]
shape_list = ["triangle", "square", "rectangle",]
quiz_history = []
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
    selected_graph = string_checker("Which shape do you want to learn about?", shape_list)
    print("You choose", selected_graph)
    print()
    formula = string_checker("you want to calculation perimeter or area ?", formula_list)
    print("You choose", formula)

    # the shape is not same so use if to use different formula

    if selected_graph == "square":
        user_answer = float(input(f"What is the {formula} of a square that has a side of {random_number1}? "))
        if formula == "perimeter":
            correct_answer = random_number1 * 4
            is_correct = check_answer(user_answer, correct_answer)
            feedback = "correct" if is_correct else "wrong"

        elif formula == "area":
            correct_answer = random_number1 * random_number1
            is_correct = check_answer(user_answer, correct_answer)
            feedback = "correct" if is_correct else "wrong"



    elif selected_graph == "triangle":
        if formula == "perimeter":
            user_answer = float(input(f"What is the {formula} of a triangle that has sides {random_number1}, {random_number2}, {random_number3}? "))
            # check user answer is correct
            correct_answer = random_number1 + random_number2 + random_number3
            is_correct = check_answer(user_answer, correct_answer)
            feedback = "correct" if is_correct else "wrong"

        elif formula == "area":
            user_answer = float(input(f"What is the {formula} of a triangle with base {random_number1} and height {random_number3}? "))
            correct_answer = (random_number1 * random_number3) / 2
            is_correct = check_answer(user_answer, correct_answer)
            feedback = "correct" if is_correct else "wrong"

    elif selected_graph == "rectangle":
        user_answer = float(input(f"What is the {formula} of a rectangle with width {random_number1} and height {random_number2}? "))

        if formula == "perimeter":
            correct_answer = 2 * (random_number1 + random_number2)
            is_correct = check_answer(user_answer, correct_answer)

            #Define feedback to ensure there is a correct value in the history.
            feedback = "correct" if is_correct else "wrong"



        elif formula == "area":
            correct_answer = random_number1 * random_number2
            is_correct = check_answer(user_answer, correct_answer)
            feedback = "correct" if is_correct else "wrong"


            print(feedback)

    # add round result to quiz history
    history_feedback = f"Round {choose}: You are {feedback}."

    # Generate history item and add it to game_history list...
    history_item = f"Round {choose}: You choose {selected_graph} {formula} and you are {feedback}."
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





