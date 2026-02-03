from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.gcd import generate_game_round


def main():

    username = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    start_game(username, generate_game_round)


if __name__ == "__main__":
    main()