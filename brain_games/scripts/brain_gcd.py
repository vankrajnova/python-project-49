#!/usr/bin/env python3

from brain_games.actions import play_game
from brain_games.games import find_gcd


def main():
    play_game(find_gcd)


if __name__ == '__main__':
    main()
