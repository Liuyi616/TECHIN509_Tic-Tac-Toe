# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import logic
from logic import *

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    num = 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = num
            num += 1
    valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    turn = 'X'
    print('Select game mode:')
    print('1.vs AI')
    print('2.vs Friend')
    mode = input('Please input your choice:')
    while mode not in ['1', '2']:
        mode = input('Wrong selection! Please select again:')
    while not winner:
        print("This is %s's turn!" % turn)
        print_board(board)
        pos = input('Please select the chess position:')
        while pos not in valid:
            pos = input('This location is invalid, please select again:')
        valid.remove(pos)
        pos = int(pos)
        row = (pos - 1) // 3
        col = (pos - 1) % 3
        board[row][col] = turn
        winner = get_winner(board)
        if mode == '1' and not winner:
            winner = ai_move(valid, board)
        else:
            turn = other_player(turn)
    print_board(board)
    if winner == 'Tie':
        print('It ends in a draw!')
    else:
        print('Game over! The winner is %s!' % winner)
