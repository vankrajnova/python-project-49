import operator
import random


RULE = 'What is the result of the expression?'


def get_game_content():
    first_number = random.randint(0, 50)
    second_number = random.randint(0, 50)

    operations = (
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
    )

    operation_name, operation_method = random.choice(operations)

    question = f'{first_number} {operation_name} {second_number}'
    correct_answer = operation_method(first_number, second_number)

    return question, correct_answer
