import prompt


def start_game(condition, game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(condition)
    counter = 0
    while counter < 3:
        question, correct_answer = game.ask_question()
        print('Question: ' + question)
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) == str(user_answer):
            print('Correct!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {user_name}!"
                  )
            break
    else:
        print(f'Congratulations, {user_name}!')
