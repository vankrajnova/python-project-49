import random

import prompt


def ask_question(value):
    print(f'Question: {value}')


def get_answer():
    return prompt.string('Your answer: ')


def show_win_message(user_name: str):
    print(f'Congratulations, {user_name}!')


def show_error_message(correct_answer, user_answer, user_name):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'."
          f"\nLet's try again, {user_name}!")


def show_correct_answer_message():
    print('Correct!')


def check_answer(user_answer, correct_answer):
    return True if correct_answer == user_answer else False


def is_answer_correct(user_name, user_answer, correct_answer):
    if user_answer == correct_answer:
        show_correct_answer_message()
        return True
    else:
        show_error_message(
            correct_answer=correct_answer,
            user_answer=user_answer,
            user_name=user_name)
        return False


def create_arithmetic_progression():
    # случайное минимальное число
    min_value = random.randint(1, 20)
    # случайное число для шага прогрессии
    step = random.randint(1, 10)
    # случайная длина списка
    random_len = random.randint(7, 12)

    list_values = [str(min_value)]

    while random_len > 1:
        value = min_value + step
        list_values.append(str(value))
        random_len -= 1
        min_value += step

    return list_values


def hide_element_in_list(list_of_elements: list):
    random_index = random.randint(0, len(list_of_elements) - 1)
    correct_answer = list_of_elements[random_index]
    list_of_elements[random_index] = '..'
    hidden_list = ' '.join(list_of_elements)
    return correct_answer, hidden_list


def is_prime(number):
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            return False
    return True
