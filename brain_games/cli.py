"""Запрашивает имя игрока."""

import prompt


def welcome_user():
    """Запрашивает имя игрока."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(name))
    return name
