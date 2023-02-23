from lib.board import TicTacBoard, SymbolEnum, ErrorEnum
from lib.inquirer import inquirer_input
from typing import Union


board: TicTacBoard = TicTacBoard()


def main() -> None:
    winner: Union[str, None] = None
    symbol_message: str = 'Would you like to use X or O for this game? [X/O]'
    symbol: str = inquirer_input(symbol_message).upper()

    if symbol != SymbolEnum.X.name and symbol != SymbolEnum.O.name:
        while True:
            print('Please choose a valid symbol for this game.')
            symbol: str = inquirer_input(symbol_message).upper()
            if symbol == SymbolEnum.X.name or symbol == SymbolEnum.O.name:
                break

    symbol_enum: SymbolEnum = SymbolEnum.X if symbol == SymbolEnum.X.name else SymbolEnum.O
    board.set_player(symbol_enum)
    print(board)

    while True:
        row: int = inquirer_input('Please select the row where you would like to make a move [0-2]', int)
        col: int = inquirer_input('Please select the column where you would like to make a move [0-2]', int)

        player_move_result: Union[ErrorEnum, None] = board.make_player_move(row, col)

        if player_move_result == ErrorEnum.MOVE_OUT_OF_BOUNDS:
            print("The spot you specified isn't on the board. Please specify another spot.")
            continue

        elif player_move_result == ErrorEnum.TAKEN_BY_BOT:
            print('The spot you selected has already been taken by the bot. Please specify another spot.')
            continue

        elif player_move_result == ErrorEnum.TAKEN_BY_PLAYER:
            print('You have selected this spot before. Please specify another spot.')
            continue

        board.make_bot_move()
        print(board)
        winner = board.check_for_winner()

        if not winner is None or board.is_board_full():
            break

    if winner == 'Player':
        print('You Won!')

    elif winner == 'Bot':
        print('The Bot Won This Time...')

    else:
        print("It's a Tie...")

    play_again_query: str = inquirer_input('Would you like to play again? [y/n]').lower()

    if play_again_query == 'y':
        board.reset_game()
        main()

    else:
        print('Till next time!')


if __name__ == '__main__':
    heading_message = f'''
    TTTTTTT  IIIIIII  CCCCCCC        TTTTTTT  AAAAAAA  CCCCCCC        TTTTTTT  OOOOOOO  EEEEEEE
       T        I     C                 T     A     A  C                 T     O     O  E
       T        I     C       =====     T     AAAAAAA  C       =====     T     O     O  EEEEEEE
       T        I     C                 T     A     A  C                 T     O     O  E
       T     IIIIIII  CCCCCCC           T     A     A  CCCCCCC           T     OOOOOOO  EEEEEEE

    ==============================================================================================
    '''
    print(heading_message)
    print("Let's play!")
    try:
        main()

    except KeyboardInterrupt:
        print('\nExiting...')
