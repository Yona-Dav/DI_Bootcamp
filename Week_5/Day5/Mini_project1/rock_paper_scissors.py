from game import Game

def get_user_menu_choice():
    print('''
    Menu
    
    1. Play a new game
    2. Show Scores
    x. Quit
    ''')

    while True:
        ans = input('Enter your choice  ')
        if ans not in '12xX':
            print('You answer is not correct')
        else:
            return ans

def print_results(results):
    print(f'''
    Game Results:
        You won {results['win']} times
        You lost {results['loss']} times
        You drew {results['draw']} times''')

def main():
    while True:
        user_choice = get_user_menu_choice()
        if user_choice == '1':
            play_game = Game()
            play_game.play()
        elif user_choice == '2':
            print_results(play_game.results)
        else:
            print('Goodbye')
            break


main()


