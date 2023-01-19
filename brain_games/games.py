import math
import random
from operator import add, sub, mul

from brain_games.actions import ask_question, get_answer, show_win_message, \
    create_arithmetic_progression, hide_element_in_list, \
    is_prime, is_answer_correct


def check_even_or_not(user_name: str):
    print('Answer "yes" if the number is even, otherwise answer "ц".')

    correct_count = 0
    while correct_count < 3:
        random_value = random.randint(0, 100)
        ask_question(value=random_value)

        answer = get_answer()

        correct_answer = 'yes' if random_value % 2 == 0 else 'no'

        if is_answer_correct(
            correct_answer=correct_answer,
            user_answer=answer,
            user_name=user_name
        ):
            correct_count += 1
        else:
            break

    if correct_count == 3:
        show_win_message(user_name=user_name)


def calculator(user_name: str):
    print('What is the result of the expression?')

    correct_count = 0
    while correct_count < 3:
        random_values = random.choices(
            [random.randint(0, 50), random.randint(0, 50)], k=2)
        random_operation = random.choices(['+', '-', '*'])

        ask_question(
            value=f'{random_values[0]} {random_operation[0]} {random_values[1]}'
        )

        if random_operation[0] == '+':
            correct_answer = add(random_values[0], random_values[1])
        elif random_operation[0] == '-':
            correct_answer = sub(random_values[0], random_values[1])
        else:
            correct_answer = mul(random_values[0], random_values[1])

        answer = get_answer()

        if is_answer_correct(
            correct_answer=correct_answer,
            user_answer=int(answer),
            user_name=user_name
        ):
            correct_count += 1
        else:
            break

    if correct_count == 3:
        show_win_message(user_name)


def find_greatest_common_divisor(user_name: str):
    print('Find the greatest common divisor of given numbers.')

    correct_count = 0

    while correct_count < 3:
        random_values = random.choices(
            [random.randint(0, 50), random.randint(0, 50)], k=2)

        ask_question(value=f'{random_values[0]} {random_values[1]}')

        correct_answer = math.gcd(random_values[0], random_values[1])

        answer = get_answer()

        if is_answer_correct(
            correct_answer=correct_answer,
            user_answer=int(answer),
            user_name=user_name
        ):
            correct_count += 1
        else:
            break

    if correct_count == 3:
        show_win_message(user_name)


def progression(user_name: str):
    print('What number is missing in the progression?')

    correct_count = 0

    while correct_count < 3:
        progression = create_arithmetic_progression()

        hidden_element, hidden_list = hide_element_in_list(progression)

        ask_question(value=f'{hidden_list}')
        answer = get_answer()

        if is_answer_correct(
            correct_answer=hidden_element,
            user_answer=answer,
            user_name=user_name
        ):
            correct_count += 1
        else:
            break

    if correct_count == 3:
        show_win_message(user_name)


def prime_number(user_name: str):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_count = 0

    while correct_count < 3:
        number = random.randint(1, 100)
        ask_question(value=f'{number}')

        answer = get_answer()

        correct_answer = 'yes' if is_prime(number) else 'no'

        if is_answer_correct(
            correct_answer=correct_answer,
            user_answer=answer,
            user_name=user_name
        ):
            correct_count += 1
        else:
            break

    if correct_count == 3:
        show_win_message(user_name)
