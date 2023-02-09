import prompt


MAX_GAME_TRIES = 3


def play_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print(game.RULE)

    for _ in range(MAX_GAME_TRIES):
        question, correct_answer = game.get_game_content()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
