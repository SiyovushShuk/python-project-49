import random
from typing import List

import prompt

from brain_games.cli import welcome_user


def make_random_number() -> int:

    return random.randint(1, 99)


def get_random_math_operation() -> str:

    operations: List[str] = ['*', '+']
    random_operation = operations[random.randint(0, len(operations) - 1)]

    return random_operation


def main():

    username = welcome_user()
    print('AWhat is the result of the expression?')

    count_queastions = 3

    for i in range(count_queastions):

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

        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')


if __name__ == "__main__":
    main()