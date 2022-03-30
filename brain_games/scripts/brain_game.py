#!/usr/bin/env python
"""Запуск основных функций."""
from brain_games.cli import welcome_user


def main():
    """Вызов основных функций программы."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
