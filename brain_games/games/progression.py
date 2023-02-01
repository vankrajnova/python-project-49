import random

RULE = 'What number is missing in the progression?'


def create_progression():
    # случайное минимальное число
    start = random.randint(1, 20)
    # случайное число для шага прогрессии
    step = random.randint(1, 10)
    # случайная длина списка
    length = random.randint(7, 12)

    # list_values = [str(min_value)]
    list_of_elements = list(range(start, (start + length * step), step))

    return list_of_elements


def hide_element_in_list(list_of_elements: list):
    random_index = random.randint(0, len(list_of_elements) - 1)

    hidden_element = list_of_elements[random_index]
    list_of_elements[random_index] = '..'
    hidden_list = ' '.join(map(str, list_of_elements))
    return hidden_element, hidden_list


def get_game_content():
    progression = create_progression()

    hidden_element, hidden_list = hide_element_in_list(progression)

    question = f'{hidden_list}'

    return question, hidden_element
