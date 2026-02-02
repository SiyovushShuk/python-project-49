from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.brain_calc import brain_calc


def main():

    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    start_game(username, brain_calc())
    

if __name__ == "__main__":
    main()