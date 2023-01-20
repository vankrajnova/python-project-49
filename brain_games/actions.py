import prompt

from brain_games.cli import welcome_user


def play_game(game):
    user_name = welcome_user()

    print(game.RULE)

    correct_count = 0

    while correct_count < 3:
        question, correct_answer = game.get_game_content()
        ask_question(value=question)

        user_answer = get_answer()

        if is_answer_correct(user_answer, correct_answer, user_name):
            correct_count += 1
        else:
            break
    if correct_count == 3:
        show_win_message(user_name)


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


def is_answer_correct(user_answer, correct_answer, user_name):
    if str(user_answer) == str(correct_answer):
        show_correct_answer_message()
        return True
    else:
        show_error_message(
            correct_answer=correct_answer,
            user_answer=user_answer,
            user_name=user_name)
        return False
