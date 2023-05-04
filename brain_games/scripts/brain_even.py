from brain_games import game_launcher
from brain_games.games.even import CONDITION
from brain_games.games import even


def main():
    game_launcher.start_game(CONDITION, even)


if __name__ == '__main__':
    main()
