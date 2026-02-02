from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.brain_gcd import brain_gcd


def main():

    username = welcome_user()
    print('What is the result of the expression?')

    start_game(username, brain_gcd)


if __name__ == "__main__":
    main()