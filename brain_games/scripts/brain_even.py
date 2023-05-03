from brain_games import game_launcher
from brain_games.games.even import CONDITION
from brain_games.games.even import ask_question


def main():
    game_launcher.start_game(CONDITION, ask_question())


if __name__ == '__main__':
    main()
