import prompt
import random


def game_condition():
    print('What number is missing in the progression?')


def ask_question():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(7, 20)
    progression = []
    for i in range(1, 11):
        num_1 += num_2
        progression.append(num_1)
    index_cut_number = random.choice(range(0, 10))
    cut_number = progression.pop(index_cut_number)
    progression.insert(index_cut_number, '..')
    question = ''
    for i in progression:
        question += str(i) + ' '
    print('Question: ' + question)
    user_answer = prompt.string('Your answer: ')
    answers_list: list[str | None] = [user_answer, cut_number]
    return answers_list


def compare_answer(answers_list, name):
    if int(answers_list[0]) == answers_list[1]:
        print('Correct!')
        return True
    else:
        wrong_answer = \
            f"'{answers_list[0]}' is wrong answer ;(. " \
            f"Correct answer was '{answers_list[1]}'." \
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
