import os

def start_game():
    player1 = 'default'
    start = 'default'
    board = ['1','2','3','4','5','6','7','8','9']
    playing = True
    turn = 1
    while player1 != 'X' and player1 != 'O':
        player1 = input('Hello would player 1 like to be X or O: ')
        if player1 == 'X' or player1 == 'O':
            break
        print("Sorry I don't recognize that. Did you want to be X or O? ")
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    while start != 'Y':
        start = input('Type Y when you are ready to get started: ')
        if start != 'Y':
            print("Sorry I don't quite understand.")
    
    while playing and turn < 10:
        if turn%2 == 0:
            player = player2
        else:
            player = player1
            
        show_board(board)
        move = get_move(board)
        board = make_move(board, player, move)
        # os.system('cls')
        # Fix clear screen
        print("******************************************")
        print("******************************************")
        playing = still_playing(board, player)
        if turn > 9:
            print("Looks like a draw. GG")
        turn += 1
        
        
        

def get_move(board):
    move = 'default'
    while move not in board:
        move = input('Choose a position for your move (1-9): ')
        if move not in board:
            print('You did not enter a valid move.')
    return int(move)

def make_move(board, player, move):
    if move in [1, 2, 3]:
        if move == 1:
            board[0] = player
        elif move == 2:
            board[1] = player
        else:
            board[2] = player
    elif move in [4, 5, 6]:
        if move == 4:
            board[3] = player
        elif move == 5:
            board[4] = player
        else:
            board[5] = player
    else:
        if move == 7:
            board[6] = player
        elif move == 8:
            board[7] = player
        else:
            board[8] = player
    return board


def show_board(board):
    row1=[' ', ' ', ' ', board[0], ' ', ' ', '|', ' ', ' ', board[1], ' ', ' ', '|', ' ', ' ', board[2], ' ', ' ', ' ']
    row2=[' ', ' ', ' ', board[3], ' ', ' ', '|', ' ', ' ', board[4], ' ', ' ', '|', ' ', ' ', board[5], ' ', ' ', ' ']
    row3=[' ', ' ', ' ', board[6], ' ', ' ', '|', ' ', ' ', board[7], ' ', ' ', '|', ' ', ' ', board[8], ' ', ' ', ' ']
    
    print('      |     |      ')
    print(''.join(row1))
    print('______|_____|______')
    print('      |     |     ')
    print(''.join(row2))
    print('______|_____|______')
    print('      |     |     ')
    print(''.join(row3))
    print('      |     |      ')


def still_playing(board, player):
    playing = True
    if board[0] == player:  
        if (board[0] == board[1] and board[0] == board[2]) or (board[0] == board[3] and board[0] == board[6]) or (board[0] == board[4] and board[0] == board[8]):
            show_board(board)
            print("Tic Tac Toe!")
            playing = False
    elif board[1] == player and (board[1] == board[4] and board[1] == board[7]):
        show_board(board)
        print("Tic Tac Toe!")
        playing = False
    elif board[2] == player:
        if (board[2] == board[4] and board[2] == board[6]) or (board[2] == board[5] and board[2] == board[8]):
            show_board(board)
            print("Tic Tac Toe!")
            playing = False
    elif board[3] == player and (board[3] == board[4] and board[3] == board[5]):
        show_board(board)
        print("Tic Tac Toe!")
        playing = False
    elif board[6] == player and (board[6] == board[7] and board[6] == board[8]):
        show_board(board)
        print("The player using "+player+" has won Tic Tac Toe!")
        playing = False
    
    return playing
    

start_game()
    