import random
from typing import List, Tuple

import prompt

from brain_games.engine import make_random_number


def _make_answer_question(progression_row: List[int]) -> Tuple[str, int]:

    random_index = random.randint(0, len(progression_row) - 1)

    answer = progression_row[random_index]

    progression_row[random_index] = ".."

    question = " ".join(map(str, progression_row))
    
    return question, answer


def _make_pregression_row(
        start_number: int, step: int, length: int
        ) -> List[int]:
    
    progression_row: List[int] = []

    for index in range(length):
        current_element = start_number + index * step
        progression_row.append(current_element)
    
    return progression_row


def generate_game_round() -> Tuple[int, int]:

    start_number = make_random_number()

    step = random.randint(1, 10)

    length_progression = random.randint(5, 12)

    progression_row = _make_pregression_row(
        start_number, step, length_progression
        )
    
    question, correct_answer = _make_answer_question(progression_row)

    print(f'Question: {question}')

    user_answer = prompt.integer('Your answer: ')

    return correct_answer, user_answer
