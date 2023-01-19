from brain_games.cli import welcome_user
from brain_games.games import progression


def main():
    user_name = welcome_user()
    progression(user_name)


if __name__ == '__main__':
    main()
