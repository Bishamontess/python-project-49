#!/usr/bin/env python3
from brain_games.scripts.greeting import greeting_user
from brain_games.scripts.get_name import get_user_name
from brain_games.scripts.games import progression


def main():
    greeting_user()
    name = get_user_name()
    progression.game_condition()
    progression.play_3_times(name)


if __name__ == '__main__':
    main()
