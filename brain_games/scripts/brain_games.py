from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')

    username = welcome_user()

    print(f'Hello, {username}!')


if __name__ == "__main__":
    main()