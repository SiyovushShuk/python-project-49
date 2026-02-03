import random
from typing import List, Tuple

import prompt

from brain_games.engine import make_random_number


def get_random_math_operation() -> str:

    operations: List[str] = ['*', '+']
    random_operation = operations[random.randint(0, len(operations) - 1)]

    return random_operation


def generate_game_round() -> Tuple[int, int]:
    first_number = make_random_number()
    second_number = make_random_number()
    math_operation = get_random_math_operation()
    
    print(f'Question: {first_number} {math_operation} {second_number}')

    match math_operation:
        case '+': 
            correct_answer = first_number + second_number

        case '*': 
            correct_answer = first_number * second_number

    user_answer = prompt.integer('Your answer: ') 

    return correct_answer, user_answer