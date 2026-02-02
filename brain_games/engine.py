import random


def make_random_number() -> int:

    return random.randint(1, 99)


def start_game(username: str, game) -> None:

    count_queastions = 3

    for i in range(count_queastions):

        correct_answer, user_answer = game()

        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')