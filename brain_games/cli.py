import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    hello = f'Hello, {user_name}!'
    print(hello)
