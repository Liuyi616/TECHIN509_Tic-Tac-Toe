from logic import *
from pandas import * 
import pandas as pd


# df = pd.read_csv('gameData.csv')

def getWins(player,df):
    counter = 0
    for i in df.loc[:,"Winner"].to_numpy():
        if i == player:
            counter+=1
    return counter

def getlosses(player,df):
    counter = 0
    for i in df.loc[:,"Loser"].to_numpy():
        if i == player:
            counter+=1
    return counter

def getDraws(df):
    counter = 0
    for i in df.loc[:,"Winner"].to_numpy():
        if i == 'Tie':
            counter+=1
    return counter

def getPoints(player,df):
    point = 0
    for i in df.loc[:,"Winner"].to_numpy():
        if i == player:
            point+=3
        if i == 'Tie':
            point+=1
    return point

def getRanks(player,df):
    if getPoints(player,df) > getPoints(other_player(player),df):
        return 1
    else:
        return 2

def getStanding(df):
    playersData = {
        'Player':['X', 'O'], 
        'Ranks': [getRanks('X',df), getRanks('O',df)], 
        'Wins' :[getWins('X',df),getWins('O',df)],  
        'Losses' :[getlosses('X',df),getlosses('0',df)], 
        'Draws':[getDraws(df), getDraws(df)], 
        'Points': [getPoints('X',df), getPoints('O',df)] 
    }
    return playersData