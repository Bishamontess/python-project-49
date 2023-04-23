import math
import prompt
import random


def ask_question():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    correct_answer = math.gcd(num_1, num_2)
    print(f'Question: {num_1} {num_2}')
    user_answer = int(prompt.string('Your answer: '))
    return correct_answer, user_answer


def compare_answer(correct_answer, user_answer):
    if correct_answer == user_answer:
        print('Correct!')
        return True
    else:
        return False


def play_3_times(name):
    counter = 0
    while counter < 3:
        correct_answer, user_answer = ask_question()
        if not compare_answer(user_answer, correct_answer):
            wrong_answer = \
                f"'{user_answer}' is wrong answer ;(. " \
                f"Correct answer was '{correct_answer}'." \
                f"\nLet's try again, {name}!"
            print(wrong_answer)
            break
        counter += 1
    else:
        print(f'Congratulations, {name}!')
