import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_content():
    random_value = random.randint(0, 100)

    correct_answer = 'yes' if random_value % 2 == 0 else 'no'
    question = f'{random_value}'

    return question, correct_answer
