from brain_games.cli import welcome_user
from brain_games.games import find_greatest_common_divisor


def main():
    user_name = welcome_user()
    find_greatest_common_divisor(user_name)


if __name__ == '__main__':
    main()
