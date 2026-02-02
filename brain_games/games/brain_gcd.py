from typing import Tuple

import prompt

from brain_games.engine import make_random_number


def find_gcd(first_num: int, second_num: int) -> int:
    while second_num != 0:
        first_num, second_num = second_num, first_num % second_num
    return first_num


def brain_gcd() -> Tuple[int, int]:

    first_random_num = make_random_number()
    second_random_num = make_random_number()

    print(f'Question: {first_random_num} {second_random_num}')

    if first_random_num > second_random_num:
        correct_answer = find_gcd(first_random_num, second_random_num)
    else:
        correct_answer = find_gcd(second_random_num, first_random_num)

    user_answer = prompt.integer('Your answer: ')

    return correct_answer, user_answer