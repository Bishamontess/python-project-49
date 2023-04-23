#!/usr/bin/env python3
from brain_games import cli
from brain_games.scripts.games import gcd


def main():
    name = cli.welcome_user()
    gcd.game_condition()
    gcd.play_3_times(name)


if __name__ == '__main__':
    main()
