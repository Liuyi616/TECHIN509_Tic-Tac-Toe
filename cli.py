# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import os
from logic import *
import numpy as np
import csv
from pandas import * 
import pandas as pd
from getStats import *

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
   
   
    winnerRecord = {'Game Mode': [mode],'Winner':[winner]}
    df1 = pd.DataFrame(winnerRecord)
    if os.path.exists("winner.csv"):  
        df1.to_csv('winner.csv', mode='a',index=False, header=False)
    else:
        df1.to_csv('winner.csv', mode='a',index=False)

    # Q1: Record all the winners in a csv file

    gameData = {
        'Game Mode': [mode],
        'Winner':[winner], 
        'Loser': [other_player(winner)], 
        'Steps of X' :[stepsCounter(board,'X')],  
        'Steps of 0' :[stepsCounter(board,'O')] 
    }

    df2 = pd.DataFrame(gameData)
    if os.path.exists("gameData.csv"):  
        df2.to_csv('gameData.csv', mode='a',index=False, header=False)
        df3 = pd.read_csv('gameData.csv')
        playersData = getStanding(df3)
    else:
        df2.to_csv('gameData.csv', mode='a',index=False)
        df3 = pd.read_csv('gameData.csv')
        playersData = getStanding(df3)

    
    df4 = pd.DataFrame(playersData)
    print("\n"+"********** Statistics to the players ********** "+"\n")
    print(df4)

    # Q2: Display any relevant statistics to the players 
    
