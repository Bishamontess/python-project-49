import prompt
import random


def ask_question():
    num = random.randint(2, 1000)
    print('Question: ' + str(num))
    for i in range(2, num):
        if num % i == 0:
            correct_answer = 'no'
            break
    else:
        correct_answer = 'yes'
    user_answer = prompt.string('Your answer: ')
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
        if not compare_answer(correct_answer, user_answer):
            wrong_answer = \
                f"'{user_answer}' is wrong answer ;(. " \
                f"Correct answer was '{correct_answer}'." \
                f"\nLet's try again, {name}!"
            print(wrong_answer)
            break
        counter += 1
    else:
        print(f'Congratulations, {name}!')
