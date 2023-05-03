import random


CONDITION = 'Answer "yes" if the number is even, ' \
            'otherwise answer "no".'


def ask_question():
    number = random.randint(0, 100)
    question = str(number)
    if number % 2 == 0:
        correct_answer = 'yes'
        return question, correct_answer
    else:
        correct_answer = 'no'
        return question, correct_answer
