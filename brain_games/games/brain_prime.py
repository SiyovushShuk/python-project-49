import math
from typing import Tuple

import prompt

from brain_games.engine import make_random_number


def is_prime_number(number: int) -> bool:

    if number < 2:
        return False
    elif number == 2:
        return True
    
    number_sqrt = int(math.sqrt(number))

    for div in range(2, number_sqrt + 1):
        if number % div == 0:
            break
    else:
        return True
    return False


def brain_prime() -> Tuple[str, str]:
    random_num = make_random_number()
    
    print(f'Question: {random_num}')

    if is_prime_number(random_num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    user_answer = prompt.string('Your answer: ')

    return correct_answer, user_answer