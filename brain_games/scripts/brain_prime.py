#!/usr/bin/env python3
from brain_games import cli
from brain_games.scripts.games import prime


def main():
    name = cli.welcome_user()
    prime.game_condition()
    prime.play_3_times(name)


if __name__ == '__main__':
    main()