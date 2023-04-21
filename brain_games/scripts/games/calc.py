import prompt
import random
import operator


def game_condition():
    print('What is the result of the expression?')


def ask_question():
    num_1 = random.randint(10, 50)
    op = random.choice(['-', '+', '*'])
    num_2 = random.randint(1, 10)
    print(f'Question: {num_1} {op} {num_2}')
    user_answer = int(prompt.string('Your answer: '))
    answers_list = []
    answers_list.append(user_answer)
    if op == '-':
        answers_list.append(operator.sub(num_1, num_2))
        return answers_list
    elif op == '+':
        answers_list.append(operator.add(num_1, num_2))
        return answers_list
    elif op == '*':
        answers_list.append(operator.mul(num_1, num_2))
        return answers_list


def compare_answer(answers_list, name):
    if answers_list[0] == answers_list[1]:
        print('Correct!')
        return True
    else:
        wrong_answer = f"'{answers_list[0]}' is wrong answer ;(. Correct answer was '{answers_list[1]}'."
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
