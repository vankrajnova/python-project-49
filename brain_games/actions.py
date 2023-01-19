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


def check_answer(answer, correct_answer):
    if correct_answer == answer:
        return True
    else:
        return False
