import random
from operator import add, sub, mul

from brain_games.actions import ask_question, get_answer, show_win_message, \
    show_error_message, show_correct_answer_message, check_answer


def check_even_or_not(user_name: str):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_count = 0
    while correct_count < 3:
        random_value = random.randint(0, 100)
        ask_question(value=random_value)

        answer = get_answer()

        correct_answer = 'yes' if random_value % 2 == 0 else 'no'

        if check_answer(answer, correct_answer):
            correct_count += 1
            show_correct_answer_message()
        else:
            show_error_message(correct_answer, answer, user_name)
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
            result = add(random_values[0], random_values[1])
        elif random_operation[0] == '-':
            result = sub(random_values[0], random_values[1])
        else:
            result = mul(random_values[0], random_values[1])

        answer = get_answer()

        if check_answer(int(answer), result):
            correct_count += 1
            show_correct_answer_message()
        else:
            show_error_message(result, answer, user_name)
            break

    if correct_count == 3:
        show_win_message(user_name)
