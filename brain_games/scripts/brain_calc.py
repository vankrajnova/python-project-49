from brain_games.cli import welcome_user
from brain_games.games import calculator


def main():
    user_name = welcome_user()
    calculator(user_name=user_name)


if __name__ == '__main__':
    main()
