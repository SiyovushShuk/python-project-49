import prompt


def welcome_user() -> str:

    username = prompt.string('May I have your name? ')

    return username