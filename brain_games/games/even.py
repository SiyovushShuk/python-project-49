from typing import Tuple

import prompt

from brain_games.engine import make_random_number


def _is_even_number(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


def generate_game_round() -> Tuple[str, str]:
    random_number = make_random_number()
    print(f'Question: {random_number}')

    if _is_even_number(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    user_answer = prompt.string('Your answer: ')

    return correct_answer, user_answer