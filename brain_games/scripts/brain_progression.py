from brain_games import game_launcher
from brain_games.games.progression import CONDITION
from brain_games.games import progression


def main():
    game_launcher.start_game(CONDITION, progression)


if __name__ == '__main__':
    main()
