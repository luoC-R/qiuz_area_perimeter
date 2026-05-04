def check_answer(user_answer, correct_answer):
    if abs(user_answer - correct_answer ) < 0.01:
        print("You are correct")
        return True
    else:
        print(f"Yu are wrong, correct answer is {correct_answer}")
        return False

user_answer = float(input("enter your answer:"))
correct_answer = 50

check_answer(user_answer, correct_answer)