#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games import check_even_or_not


def main():
    user_name = welcome_user()
    check_even_or_not(user_name=user_name)


if __name__ == '__main__':
    main()