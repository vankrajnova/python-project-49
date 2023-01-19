import random
import prompt


def check_even_or_not(name: str):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_count = 0
    while correct_count < 3:
        random_value = random.randint(0, 100)
        print(f'Question: {random_value}')
        answer = prompt.string('Your answer: ')
        if random_value % 2 == 0 and answer == 'yes':
            correct_count += 1
            print('Correct!')
        elif random_value % 2 != 0 and answer == 'no':
            correct_count += 1
            print('Correct!')
        else:
            correct_answer = 'no' if answer == 'yes' else 'yes'
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
    if correct_count == 3:
        print(f'Congratulations, {name}!')
