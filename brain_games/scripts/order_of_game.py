

from brain_games.scripts.greeting import greeting_user
from brain_games.scripts.get_name import get_user_name
from brain_games.scripts.games import



def play_3_times(user_name):
    counter = 0
    while counter < 3:
        if not compare_result():
            break
        counter += 1
    else:
        print('Congratulations, ' + user_name)

def main():
    greeting_user()
    name = get_user_name()
    game_condition()
    play_3_times(name)
