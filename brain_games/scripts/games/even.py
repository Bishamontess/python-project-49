import prompt
import random


def ask_question():
    number = random.randint(0, 100)
    answers_list = []
    if number % 2 == 0:
        answers_list.append('yes')
    else:
        answers_list.append('no')
    question = f'Question: {number}'
    print(question)
    user_answer = prompt.string('Your answer: ')
    answers_list.append(user_answer)
    return answers_list


def compare_answer(answers_list):
    if answers_list[0] == answers_list[1]:
        print('Correct!')
        return True
    else:
        return False


def play_3_times(name):
    counter = 0
    while counter < 3:
        answers_list = ask_question()
        if not compare_answer(answers_list):
            wrong_answer = \
                f"'{answers_list[1]}' is wrong answer ;(. " \
                f"Correct answer was '{answers_list[0]}'." \
                f"\nLet's try again, {name}!"
            print(wrong_answer)
            break
        counter += 1
    else:
        print(f'Congratulations, {name}!')
