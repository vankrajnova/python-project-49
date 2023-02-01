import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number > 1:
        for n in range(2, number):
            if (number % n) == 0:
                # is not a prime number
                return False
        # is a prime number
        return True
    else:
        # is not a prime number
        return False


def get_game_content():
    random_number = random.randint(1, 100)

    question = f'{random_number}'
    correct_answer = 'yes' if is_prime(random_number) else 'no'

    return question, correct_answer
