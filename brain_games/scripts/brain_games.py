#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.games import gcd
from brain_games.scripts.games import calc
from brain_games.scripts.games import even
from brain_games.scripts.games import prime
from brain_games.scripts.games import progression


def brain_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. '
          'Otherwise answer "no".')
    prime.play_3_times(name)


def brain_gcd():
    name = welcome_user()
    print('Find the greatest common '
          'divisor of given numbers.')
    gcd.play_3_times(name)


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even.play_3_times(name)


def brain_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    progression.play_3_times(name)


def brain_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    calc.play_3_times(name)


def main():
    welcome_user()


if __name__ == '__main__':
    main()
