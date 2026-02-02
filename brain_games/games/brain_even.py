from typing import Tuple

import prompt

from brain_games.engine import make_random_number


def is_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False


def brain_even() -> Tuple[str, str]:
    random_number = make_random_number()
    print(f'Question: {random_number}')

    if is_even_number(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    user_answer = prompt.string('Your answer: ')

    return correct_answer, user_answer