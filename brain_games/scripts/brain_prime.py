from brain_games.cli import welcome_user
from brain_games.games import prime_number


def main():
    user_name = welcome_user()
    prime_number(user_name)


if __name__ == '__main__':
    main()
