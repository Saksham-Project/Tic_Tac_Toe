'''
This is a tic tac toe 
But this time you will be playing against a weak computer 

level: easy
'''

'''
This is a tic tac toe but you are going to play with machine
'''

import random
import time

def print_board():

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print('---|---|---')
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print('---|---|---')
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def update_board(choice,symbol):
    if board[choice] == ' ':
        board[choice] = symbol
        print_board()
        return True
    else:
        print('space is already occupied.')
        
        
def winning_moves(symbol):
    win_move = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for move in win_move:
        if board[move[0]] == board[move[1]] == board[move[2]] == symbol :
            return True

    return False

def win_decide(symbol):
    if winning_moves(symbol):
        print(f"{symbol} wins")
        exit()
    elif ' ' not in board:
        print('Game draw')
        exit()

def play():
    value = 1
    while True:
        try:
            if value == 1:
                print('Player(X) turn')
                player_choice = int(input('Enter number between (1-9): ')) - 1
                if 0 <= player_choice <= 8:
                    if update_board(player_choice,'X'):   
                        value -= 1
                    else:
                        continue

                    win_decide('X')

                else:
                    print('Enter a valid value(1-9)')
                    continue
            if value != 1:
                print('AI(O) turn')
                AI_choice = random.choice(AI)
                
                time.sleep(0.8)

                if update_board(AI_choice,'O'):
                    value += 1  
                else:
                    continue

                win_decide('O')

            

        except ValueError:
            print('Enter a valid value (1-9)')
            continue

print('Welcome to tic tac toe')
print('Your opponent is weak computer')
print('level easy')

board = [' ' for _ in range(9)]
AI = [0,1,2,3,4,5,6,7,8]
print_board()
play()