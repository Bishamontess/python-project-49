import prompt
import random


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
    correct_answer = max(dividers_num_1.intersection(dividers_num_2))
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
