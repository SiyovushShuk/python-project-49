from random import randint

import prompt

from brain_games.cli import welcome_user


def make_random_number() -> int:

    return randint(1, 99)


def is_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False
    

def main():

    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count_queastions = 3

    for i in range(count_queastions):

        random_number = make_random_number()
        print(f'Question: {random_number}')

        if is_even_number(random_number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        user_answer = prompt.string('Your answer: ')

        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {username}")
            break
    else:
        print(f'Congratulations, {username}!')


if __name__ == "__main__":
    main()