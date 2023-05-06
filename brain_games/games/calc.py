import random
import operator


GAME_RULE = 'What is the result of the expression?'


def get_game():
    question, correct_answer = calculate_expression()
    return question, correct_answer


def calculate_expression():
    num_1 = random.randint(10, 50)
    op = random.choice(['-', '+', '*'])
    num_2 = random.randint(1, 10)
    question = str(num_1) + ' ' + str(op) + ' ' + str(num_2)
    if op == '-':
        correct_answer = operator.sub(num_1, num_2)
        return question, correct_answer
    elif op == '+':
        correct_answer = operator.add(num_1, num_2)
        return question, correct_answer
    elif op == '*':
        correct_answer = operator.mul(num_1, num_2)
        return question, correct_answer
