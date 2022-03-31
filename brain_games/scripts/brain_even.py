#!/usr/bin/env python
from random import randint
from brain_games.cli import welcome_user

import prompt


def even_question(a):
    """Игра на определение четности числа"""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    total_correct = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while total_correct != a:
        number = randint(0, 100)
        print("Question: {0}".format(number))
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer == "yes":
            print('Correct!')
            total_correct += 1
        elif number % 2 != 0 and answer == "no":
            print('Correct!')
            total_correct += 1
        else:
            print(''''yes' is wrong answer ;(. Correct answer was 'no'. \n
Let's try again, {0}!'''.format(name))
            return 0
    print('Congratulations, {0}!'.format(name))


def main():
    even_question(3)


if __name__ == '__main__':
    main()
