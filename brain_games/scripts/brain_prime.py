from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.brain_prime import brain_prime


def main():

    username = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    start_game(username, brain_prime)


if __name__ == "__main__":
    main()