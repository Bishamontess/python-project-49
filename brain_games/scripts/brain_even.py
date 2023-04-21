#!/usr/bin/env python3
from brain_games.scripts.greeting import greeting_user
from brain_games.scripts.get_name import get_user_name
from brain_games.scripts.games import even


def main():
    greeting_user()
    name = get_user_name()
    even.game_condition()
    even.play_3_times(name)


if __name__ == '__main__':
    main()
