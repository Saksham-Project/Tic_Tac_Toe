'''
Ladies and gentelment,
Here I present you a basic tic tac toe game.

Hope you enjoy it.
'''
def show_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def update_board(choice,symbol):
    if board[choice] == ' ':
        board[choice] = symbol
        show_board()
        return True
    else:
        print('space is already occupied')
       
        


def winning_moves(symbol):
    win_move = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for move in win_move:
        if board[move[0]] == board[move[1]] == board[move[2]] == symbol:
            return True
    return False

def win_decide(player):
    if winning_moves(player):
        print(f"{player} wins")
        exit()
    elif ' ' not in board:
        print('Game draw')
        exit()


def play():
    value = 1
    while True:
        
        try:
            if value == 1:

                print("X's turn")
                x_choice = int(input('Enter the number between(1-9): ')) - 1

                if 0 <= x_choice <= 8:
                    if update_board(x_choice,'X'):
                        value -= 1
                    else:
                        continue
                    win_decide('X')
                else:
                    print('please enter number between(1-9)')
            
            elif value != 1:
                print("O's turn ")
                o_choice = int(input('Enter the number between(1-9): ')) - 1
                
                if 0 <= o_choice <= 8:
                    if update_board(o_choice,'O'):
                        value  += 1
                    else:
                        continue
                    win_decide('O')

                else:
                    print('please, enter number between(1-9): ')

        except ValueError:
            print('please input valid value (1-9)')
                
print('\n')
print('Welcome to tic tac toe')

board = [' ' for _ in range(9)]
show_board()
play()