#!/usr/bin/env python3
from brain_games import cli
from brain_games.scripts.games import progression


def main():
    name = cli.welcome_user()
    progression.game_condition()
    progression.play_3_times(name)


if __name__ == '__main__':
    main()
