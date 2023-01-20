#!/usr/bin/env python3

from brain_games.actions import play_game
from brain_games.games import prime_numbers


def main():
    play_game(prime_numbers)


if __name__ == '__main__':
    main()
