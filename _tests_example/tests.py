import math
import random

import prompt
from operator import add, sub, mul


def calc():
    name = 'John'

    correct_count = 0

    while correct_count < 3:
        random_values = random.choices([random.randint(0, 50), random.randint(0, 50)], k=2)
        random_operation = random.choices(['+', '-', '*'])

        print(f'Question: {random_values[0]} {random_operation[0]} {random_values[1]}')

        if random_operation[0] == '+':
            result = add(random_values[0], random_values[1])
        elif random_operation[0] == '-':
            result = sub(random_values[0], random_values[1])
        else:
            result = mul(random_values[0], random_values[1])

        answer = prompt.string('Your answer: ')

        if result == int(answer):
            print('Correct!')
            correct_count += 1
        else:

            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'."
                  f"\nLet's try again, {name}!")
            break


if __name__ == '__main__':
    calc()