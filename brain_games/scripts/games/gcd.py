import prompt
import random


def game_condition():
    print('Find the greatest common divisor of given numbers.')


def ask_question():
    num_1 = random.randint(0, 100)
    # find all dividers for num_1, add them to the list
    dividers_num_1 = set()
    for i in range(1, int(num_1 + 1)):
        if num_1 % i == 0:
            dividers_num_1.add(i)
    num_2 = random.randint(0, 100)
    # find all dividers for num_2, add them to the list
    dividers_num_2 = set()
    for i in range(1, int(num_2 + 1)):
        if num_2 % i == 0:
            dividers_num_2.add(i)
    # unite both divider's sets in joint set of dividers
    cross_dividers = dividers_num_1.intersection(dividers_num_2)
    # find the largest divisor
    correct_answer = max(cross_dividers)
    print(f'Question: {num_1} {num_2}')
    user_answer = int(prompt.string('Your answer: '))
    answers_list = [correct_answer, user_answer]
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
