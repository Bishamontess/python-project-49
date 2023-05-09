from random import choice, randint
from operator import sub, mul, add


GAME_RULE = 'What is the result of the expression?'


def get_game():
    num_1 = randint(10, 50)
    op = choice(['-', '+', '*'])
    num_2 = randint(1, 10)
    question = str(num_1) + ' ' + str(op) + ' ' + str(num_2)
    correct_answer = calculate_expression(num_1, num_2, op)
    return question, correct_answer


def calculate_expression(num_1, num_2, op):
    if op == '-':
        correct_answer = sub(num_1, num_2)
        return correct_answer
    elif op == '+':
        correct_answer = add(num_1, num_2)
        return correct_answer
    elif op == '*':
        correct_answer = mul(num_1, num_2)
        return correct_answer
