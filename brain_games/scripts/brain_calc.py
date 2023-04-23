#!/usr/bin/env python3
from brain_games.scripts.brain_games import welcome_user
from brain_games.scripts.games import calc


def main():
    name = welcome_user()
    calc.game_condition()
    calc.play_3_times(name)


if __name__ == '__main__':
    main()
