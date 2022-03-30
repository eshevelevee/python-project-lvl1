import prompt


def welcome_user():
    """Запрашивает имя игрока."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    
