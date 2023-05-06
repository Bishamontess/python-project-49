import random


GAME_RULE = 'Answer "yes" if given number is prime. ' \
            'Otherwise answer "no".'


def get_game():
    answer = is_prime()
    if answer[0]:
        correct_answer = 'yes'
        return str(answer[1]), correct_answer
    else:
        correct_answer = 'no'
        return str(answer[1]), correct_answer


def is_prime():
    num = random.randint(1, 1000)
    for i in range(2, num):
        if num % i == 0:
            return False, num
        else:
            continue
    else:
        return True, num
