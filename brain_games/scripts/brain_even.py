#!/usr/bin/env python3
from brain_games.scripts.games.even import play_3_times
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play_3_times(name)


if __name__ == '__main__':
    main()
