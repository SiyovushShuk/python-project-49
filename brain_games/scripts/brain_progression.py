from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.brain_progression import brain_progression


def main():

    username = welcome_user()
    print('What number is missing in the progression?')

    start_game(username, brain_progression)


if __name__ == "__main__":
    main()