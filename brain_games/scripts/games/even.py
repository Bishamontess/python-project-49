import prompt
import random


def game_condition():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def ask_question():
    number = random.randint(0, 100)
    answers_list = []
    answers_list.append(number)
    question = f'Question: {number}'
    print(question)
    user_answer = prompt.string('Your answer: ')
    answers_list.append(user_answer)
    return answers_list


def compare_answer(answers_list, name):
    if answers_list[0] % 2 == 0:
        correct_answer = 'yes'
        if correct_answer == answers_list[1]:
            print('Correct!')
            return True
        else:
            wrong_answer = f"'{answers_list[1]}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            again = f"\nLet's try again, {name}!"
            try_again = wrong_answer + again
            print(try_again)
            return False
    elif answers_list[0] % 2 != 0:
        correct_answer = 'no'
        if correct_answer == answers_list[1]:
            print('Correct!')
            return True
        else:
            wrong_answer = f"'{answers_list[1]}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            again = f"\nLet's try again, {name}!"
            try_again = wrong_answer + again
            print(try_again)
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
