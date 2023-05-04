from brain_games import game_launcher
from brain_games.games.prime import CONDITION
from brain_games.games import prime


def main():
    game_launcher.start_game(CONDITION, prime)


if __name__ == '__main__':
    main()
