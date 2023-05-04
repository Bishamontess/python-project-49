from brain_games import game_launcher
from brain_games.games.gcd import CONDITION
from brain_games.games import gcd


def main():
    game_launcher.start_game(CONDITION, gcd)


if __name__ == '__main__':
    main()
