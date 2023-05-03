import random


CONDITION = 'Answer "yes" if given number is prime. ' \
            'Otherwise answer "no".'


def ask_question():
    num = random.randint(2, 1000)
    question = str(num)
    for i in range(2, num):
        if num % i == 0:
            correct_answer = 'no'
            return question, correct_answer
        else:
            correct_answer = 'yes'
            return question, correct_answer
