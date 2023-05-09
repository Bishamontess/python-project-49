import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULE)
    counter = 0
    while counter < 3:
        question, correct_answer = game.get_game()
        print('Question: ' + question)
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) == str(user_answer):
            print('Correct!')
            counter += 1
        else:
            return \
                print(f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'."
                      f"\nLet's try again, {user_name}!"
                      )
    print(f'Congratulations, {user_name}!')
