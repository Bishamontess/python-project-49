import random


CONDITION = 'What number is missing ' \
            'in the progression?'


def ask_question():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(7, 20)
    progression = []
    for i in range(1, 11):
        num_1 += num_2
        progression.append(num_1)
    index_cut_number = random.choice(range(0, 10))
    correct_answer = progression.pop(index_cut_number)
    progression.insert(index_cut_number, '..')
    question = ''
    for i in progression:
        question += str(i) + ' '
    return question, correct_answer
