from enum import Enum
from typing import Union
from random import randint


class SymbolEnum(Enum):
    DEFAULT = 0
    X = 1
    O = 2


class ErrorEnum(Enum):
    INVALID_PLAYER = 0
    TAKEN_BY_BOT = 1
    TAKEN_BY_PLAYER = 2
    MOVE_OUT_OF_BOUNDS = 3
    PLAYER_AND_BOT_NOT_SET = 4
    BOARD_IS_FULL = 5


class TicTacBoard:
    def __init__(self) -> None:
        self.__player: SymbolEnum = SymbolEnum.DEFAULT
        self.__bot: SymbolEnum = SymbolEnum.DEFAULT
        self.__board: list[list[str]] = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def __repr__(self) -> str:
        board = self.__board
        board_block: str = f'''
            0     1     2
               |     |
         0  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}
          _____|_____|_____
               |     |
         1  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}
          _____|_____|_____
               |     |
         2  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}
               |     |

        '''

        return board_block

    def __make_move(self, row: int, column: int, symbol: str) -> Union[ErrorEnum, None]:
        if self.is_board_full():
            return ErrorEnum.BOARD_IS_FULL
        if self.__player == SymbolEnum.DEFAULT and self.__bot == SymbolEnum.DEFAULT:
            return ErrorEnum.PLAYER_AND_BOT_NOT_SET
        if (row < 0 or row > len(self.__board)) or (column < 0 or column > len(self.__board[row])):
            return ErrorEnum.MOVE_OUT_OF_BOUNDS
        if self.__board[row][column] == self.__bot.name:
            return ErrorEnum.TAKEN_BY_BOT
        if self.__board[row][column] == self.__player.name:
            return ErrorEnum.TAKEN_BY_PLAYER

        self.__board[row][column] = symbol

    def set_player(self, player: SymbolEnum) -> Union[ErrorEnum, None]:
        if player != SymbolEnum.X and player != SymbolEnum.O:
            return ErrorEnum.INVALID_PLAYER
        self.__player = player
        self.__bot = SymbolEnum.X if player == SymbolEnum.O else SymbolEnum.O

    def make_player_move(self, row: int, column: int) -> Union[ErrorEnum, None]:
        return self.__make_move(row, column, self.__player.name)

    def make_bot_move(self) -> None:
        row: int = randint(0, 2)
        column: int = randint(0, 2)
        move: Union[ErrorEnum, None] = self.__make_move(row, column, self.__bot.name)
        if move != None and move != ErrorEnum.BOARD_IS_FULL and move != ErrorEnum.PLAYER_AND_BOT_NOT_SET:
            self.make_bot_move()

    def check_for_winner(self) -> Union[str, None]:
        winning_combinations: list[list[list[int]]] = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]]
        ]

        for combination in winning_combinations:
            value1 = self.__board[combination[0][0]][combination[0][1]]
            value2 = self.__board[combination[1][0]][combination[1][1]]
            value3 = self.__board[combination[2][0]][combination[2][1]]

            if value1 == self.__player.name and value2 == self.__player.name and value3 == self.__player.name:
                return 'Player'
            elif value1 == self.__bot.name and value2 == self.__bot.name and value3 == self.__bot.name:
                return 'Bot'

        return None

    def is_board_full(self) -> bool:
        for row in self.__board:
            for col in row:
                if col == ' ':
                    return False

        return True

    def reset_game(self):
        self.__player: SymbolEnum = SymbolEnum.DEFAULT
        self.__bot: SymbolEnum = SymbolEnum.DEFAULT
        self.__board: list[list[str]] = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
