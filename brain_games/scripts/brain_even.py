#!/usr/bin/env python
"""Игра в определение четности числа."""

from random import randint
import prompt
from brain_games.cli import welcome_user


def even_question(number_of_tries):
    """Игра на определение четности числа.

    :param number_of_tries: количество успешных попыток подряд для выигрыша
    :type number_of_tries: int
    :return: 0 если игрок ошибся
    """
    print('Welcome to the Brain Games!')
    name = welcome_user()
    total_correct = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while total_correct != number_of_tries:
        number = randint(0, 100)
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer == 'yes':
            print('Correct!')
            total_correct += 1
        elif number % 2 != 0 and answer == 'no':
            print('Correct!')
            total_correct += 1
        else:
            message = """
'yes' is wrong answer ;(. Correct answer was 'no'. \n
Let's try again, {0}!
""".format(name)
            print(message)
            return 0
    print('Congratulations, {0}!'.format(name))


def main():
    """Запуск игры"""
    even_question(3)


if __name__ == '__main__':
    main()
