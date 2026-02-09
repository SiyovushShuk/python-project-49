import random
from typing import Any, Tuple


def make_random_number(start: int = 0, end: int = 99) -> int:
    '''
    Function generate random number in the range from start to end.

    @param start: number start range for generate random number. Default num 0.
    :type start: int

    @param end: end number range for generate random number. Default num 99.
    :type end: int

    :return: return random number in the range from start to end.
    :rtype: int
    '''

    return random.randint(start, end)  # NOSONAR


def start_game(
        username: str,
        game_round: Tuple[Any, Any],
        numbers_game_round: int = 3
        ) -> None:
    '''
    Function start game, check user answers.
    Depending on the answer, the user sends a response.  
    
    @param username: Username of player
    :type username: str

    @param numbers_game_round: Numbers of game round. Default game has 3 rounds.
    :type numbers_game_round: int

    @param game_round: Function of game round. Realize game logic. Print question, get user answer and find correct answer. Give back in first param correct answer, second answer user answer.
    :type game_round: Tuple[Any, Any]

    :return: function sends result of processing response 
    '''  # noqa: E501

    numbers_game_round = 3

    for i in range(numbers_game_round):

        correct_answer, user_answer = game_round()

        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')