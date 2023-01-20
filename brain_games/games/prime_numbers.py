import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            return False
    return True


def get_game_content():
    random_number = random.randint(1, 100)

    question = f'{random_number}'
    correct_answer = 'yes' if is_prime(random_number) else 'no'

    return question, correct_answer
