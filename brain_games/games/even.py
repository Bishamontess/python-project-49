import random


GAME_RULE = 'Answer "yes" if the number is even, ' \
            'otherwise answer "no".'


def get_game():
    answer = is_even()
    if answer[0] is True:
        correct_answer = 'yes'
        return str(answer[1]), correct_answer
    else:
        correct_answer = 'no'
        return str(answer[1]), correct_answer


def is_even():
    number = random.randint(0, 100)
    if number % 2 == 0:
        return True, number
    else:
        return False, number
