#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    global user_name
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')


def is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
            if correct_answer == str(user_answer):
                print('Correct!')
            else:
                correct_answer1 = f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
                print(correct_answer1)
                correct_answer2 = f"Let's try again, {user_name}!"
                print(correct_answer2)
                break
        elif number % 2 != 0:
            correct_answer = 'no'
            if correct_answer == str(user_answer):
                print('Correct!')
            else:
                correct_answer1 = f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
                print(correct_answer1)
                correct_answer2 = f"Let's try again, {user_name}!"
                print(correct_answer2)
                break
        counter += 1
    else:
        print('Congratulations, ' + user_name)


def main():
    welcome_user()
    is_even()


if __name__ == '__main__':
    main()
