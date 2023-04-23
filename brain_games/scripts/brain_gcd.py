#!/usr/bin/env python3
from brain_games import cli
from brain_games.scripts.games import gcd


def main():
    name = cli.welcome_user()
    print('Find the greatest common '
          'divisor of given numbers.')
    gcd.play_3_times(name)


if __name__ == '__main__':
    main()
