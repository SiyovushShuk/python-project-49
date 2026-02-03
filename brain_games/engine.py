import random
from typing import Any, Tuple


def make_random_number() -> int:
    '''
    Function generate random number in the range from 0 to 99.
    
    :return: return random number in the range from 0 to 99.
    :rtype: int
    '''

    return random.randint(0, 99)


def start_game(
        username: str,
        game_round: Tuple[Any, Any],
        count_queastions: int = 3
        ) -> None:
    '''
    Function start game, check user answers.
    Depending on the answer, the user sends a response.  
    
    @param username: Username of player
    :type username: str

    @param count_queastions: Numbers of game round. Default game has 3 rounds.
    :type count_queastions: int

    @param game_round: Function of game round. Realize game logic. Print question, get user answer and find correct answer. Give back in first param correct answer, second answer user answer.
    :type game_round: Tuple[Any, Any]

    :return: function sends result of processing response 
    '''  # noqa: E501

    count_queastions = 3

    for i in range(count_queastions):

        correct_answer, user_answer = game_round()

        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')