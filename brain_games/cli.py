import prompt


def welcom_user() -> str:

    username = prompt.string('May I have your name? ')

    return username