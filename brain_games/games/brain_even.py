from brain_games.engine import make_random_number


def is_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False


def brain_even():
    random_number = make_random_number()
    print(f'Question: {random_number}')

    if is_even_number(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return correct_answer