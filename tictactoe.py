def display_board(board):
    
    print(' ' +board[1]+ '|' +board[2]+ '|' +board[3])
    print('––|–|––')
    print(' ' +board[4]+ '|' +board[5]+ '|' +board[6])
    print('––|–|––')
    print(' ' +board[7]+ '|' +board[8]+ '|' +board[9])

def player_input():
    
    choice = 'wrong'
    
    while choice not in ['X', 'O']:
        choice = input('Player 1: Do you want to be X or O? ')
        
        if choice not in ['X', 'O']:
            print('Invalid selection, please try again!')
        
        
        player1 = choice
        
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
            
            
    return player1, player2  

def place_marker(board, marker, position):
    
    marker_player1, marker_player2 = player_input()
    
    #Checks to see if position is in range, will keep asking for position until it is valid
    
    while position not in range(1,10):
        
        print('That is not a valid position. Please try again.')
        
        position = int(input('Choose your next position (1-9): '))
        
        
    # If input is valid, assigns marker to index position of input in board
    if position in range(1,10):
        board[position] = marker   

def win_check(board, mark):
    
    #checks if first row is the same
    if board[1] == mark and board[2]== mark and board[3] == mark:
        return True
        
    #checks if diagonal right is same    
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    
    #diagnoal left
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    
    #checks second row
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
        
    #checks third row
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    
    #down the left
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    
    #down the middle
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    
    #down the right
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
        
    else:
        return False

import random

def choose_first():
    first_player = 1
    second_player = 2
    chosen = random.randint(1,2)
    if chosen == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
        
    return board[position] == ' '
    
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    
    position = int(input('Choose your next position (1-9): '))
        
    while space_check(board, position) == False:
            print('This position has already been taken, please try again.')
            position = int(input('Choose your next position (1-9): '))
            
    else:
        return position

def replay():
    
    replay = True
    
    game_on = input('Do you want to play again? (Y/N): ')
    
    while game_on not in ['Y', 'N']:
        print('Please type "Y" or "N".')
        game_on = input('Do you want to play again? (Y/N): ')
        
    if game_on == 'Y':
        return True
    else: 
        return False

        

print('Welcome to Tic Tac Toe!\n')

while True:
    
    game_board = [' '] * 10

# Players choose markers:    
    markerp1, markerp2 = player_input()

    turn = choose_first()
    print(turn + ' will go first\n')

    ready_to_play = input('Are you ready to play? Enter "yes" or "no". ')
    if ready_to_play.lower() == 'yes':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        #Player1's turn
        if turn == 'Player 1':
            display_board(game_board)
            print("Player 1, it's your turn\n")
            position = player_choice(game_board)
            place_marker(game_board, markerp1, position)
            print('\n' *100)
            #Checks if game has been won
            if win_check(game_board, markerp1):
                display_board(game_board)
                print('Game over. Player 1 wins the game!')
                game_on = False
        
            #Checks if it's a tie
            elif full_board_check(game_board):
                display_board(game_board)
                print("Game over. It's a tie!")

            #Changes who's turn it is: 
            else:
                turn = 'Player 2'    
   
        #Player2's turn        
        else:
            print("Player 2, it's your turn.\n")
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, markerp2, position)
            print('\n' *100)
                #Checks if game has been won
            if win_check(game_board, markerp2):
                    display_board(game_board)
                    print('Game over. Player 2 wins the game!')
                    game_on = False
                
                #Checks if it's a tie    
            elif full_board_check(game_board):
                    display_board(game_board)
                    print("Game over. It's a tie!")
                    game_on = False

                #Changes who's turn it is:    
            else:
                    turn = 'Player 1'

                    

    keep_playing = replay()
    if not keep_playing:
        break
    
    