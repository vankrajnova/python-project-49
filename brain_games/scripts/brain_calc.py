#!/usr/bin/env python3
from brain_games.actions import play_game
from brain_games.games import calc


def main():
    play_game(calc)


if __name__ == '__main__':
    main()
