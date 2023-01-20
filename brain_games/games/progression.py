import random

RULE = 'What number is missing in the progression?'


def create_progression():
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

    hidden_element = list_of_elements[random_index]
    list_of_elements[random_index] = '..'
    hidden_list = ' '.join(list_of_elements)
    return hidden_element, hidden_list


def get_game_content():
    progression = create_progression()

    hidden_element, hidden_list = hide_element_in_list(progression)

    question = f'{hidden_list}'

    return question, hidden_element
