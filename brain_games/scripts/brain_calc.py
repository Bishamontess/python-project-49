from brain_games import game_launcher
from brain_games.games.calc import CONDITION
from brain_games.games import calc


def main():
    game_launcher.start_game(CONDITION, calc)


if __name__ == '__main__':
    main()
