import prompt
import random


def game_condition():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def ask_question():
    num = random.randint(2, 1001)
    print('Question: ' + str(num))
    answers_list = []
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                answers_list.append('no')
                break
        else:
            answers_list.append('yes')
    else:
        answers_list.append('yes')
    user_answer = prompt.string('Your answer: ')
    answers_list.append(user_answer)
    return answers_list


def compare_answer(answers_list, name):
    if answers_list[0] == answers_list[1]:
        print('Correct!')
        return True
    else:
        wrong_answer = \
            f"'{answers_list[1]}' is wrong answer ;(. " \
            f"Correct answer was '{answers_list[0]}'." \
            f"\nLet's try again, {name}!"
        print(wrong_answer)
        return False


def play_3_times(name):
    counter = 0
    while counter < 3:
        answers_list = ask_question()
        if not compare_answer(answers_list, name):
            break
        counter += 1
    else:
        print(f'Congratulations, {name}!')
