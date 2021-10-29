moves = [
[' ',' ',' '],
[' ',' ',' '],
[' ',' ',' ']]

def display_board():
    board = f'''
    *************
    * {moves[0][0]} | {moves[0][1]} | {moves[0][2]} *
    * --|---|-- *
    * {moves[1][0]} | {moves[1][1]} | {moves[1][2]} *
    * --|---|-- *
    * {moves[2][0]} | {moves[2][1]} | {moves[2][2]} *
    *************
    '''
    return board



def play():
    count = 0
    turn = 'X'

    for i in range(10):
        print(display_board())
        print(f'Player {turn}\'s turn ...')
        row = int(input('Enter row  '))
        column = int(input('Enter column  '))
        if moves[row-1][column-1]==' ':
            moves[row-1][column-1]=turn
            count+=1
        else:
            print("This place in not empty")
            continue



        if count>4:
            if moves[0][0]==moves[0][1]==moves[0][2]!=' ':
                print(display_board())        
                print("\nGame Over.\n")                
                print(turn + " won.")                
                break
            elif moves[1][0]==moves[1][1]==moves[1][2]!=' ':
                print(display_board())        
                print("\nGame Over.\n")                
                print(turn + " won.")                
                break
            elif moves[2][0]==moves[2][1]==moves[2][2]!=' ':
                print(display_board())        
                print("\nGame Over.\n")                
                print(turn + " won.")                
                break
            elif moves[0][0]==moves[1][0]==moves[2][0]!=' ':
                print(display_board())        
                print("\nGame Over.\n")                
                print(turn + " won.")                
                break
            elif moves[0][1]==moves[1][1]==moves[2][1]!=' ':
                print(display_board())        
                print("\nGame Over.\n")                
                print(turn + " won.")                
                break
            elif moves[0][2]==moves[1][2]==moves[2][2]!=' ':
                print(display_board())        
                print("\nGame Over.\n")                
                print(turn + " won.")                
                break
            elif moves[0][0]==moves[1][1]==moves[2][2]!=' ':
                print(display_board())        
                print("\nGame Over.\n")                
                print(turn + " won.")                
                break
            elif moves[2][0]==moves[1][1]==moves[0][2]!=' ':
                print(display_board())        
                print("\nGame Over.\n")                
                print(turn + " won.")                
                break

        if turn =='X':
            turn='O'
        else:
            turn='X'
        
        if count==9:
            print("\nGame Over.\n")                
            print("It is a Tie!") 
            return(play_again())


def play_again():
    
    play_again= input('Do you want to play again ? Enter yes or no ')
    if play_again=='yes':
        for i in len(moves):
            for j in len(moves[0]):
                moves[i][j]=' '
        
        return play()
    else:
        print('Ok! Bye Bye!')


play()