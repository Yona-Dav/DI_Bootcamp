# hangman_body=head + body+left_arm + right_arm+left_leg+right_leg

import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']

word=''


hangman_draw= ['''
     +----
         |
         |
         |  
        ---''', '''
     +----
     O   |
         |
         |  
        ---''','''
     +----
     O   |
     |   |
         |  
        ---''','''  
     +----
     O   |
    /|   |
         |  
        ---''','''
     +----
     O   |
    /|\  |
         |  
        ---''','''
     +----
     O   |
    /|\  |
    /    |  
        ---''','''
     +----
     O   |
    /|\  |
    / \  |  
        ---'''

]

def display_stars():
    word = random.choice(wordslist)
    return word

def play_game():
    word = display_stars()
    stars = '*'*len(word)
    count = 0
    letters=[]
    l=''
    guess = False
    print(stars)

    while guess==False and count<6:
        print(letters)
        l= input("Enter a letter").lower()
        if len(l)==1 and l.isalpha():
            if l in letters:
                print('You already tried this letter')

            else:
                letters.append(l)
                for i in range(len(word)):
                    if word[i]==l:
                        new_stars = stars[:i]+l+stars[i+1:]
                        stars = new_stars
                        print(stars)
                if l not in word:
                    count +=1
                    print(f'You have {6-count} chances left')
                    print(stars)
                    print(hangman_draw[count])
        else:
            print("Invalid Input")
        

        if stars == word:
            print('You Win')
            guess=True
            return (play_again())

    
        if (6-count )==0:
            print('You lose')
            print(f"The word was {word}")
            return (play_again())
        
    


def play_again():
    play_again= input('Do you want to play again ? Enter yes or no ')
    if play_again=='yes':        
        return play_game()
    else:
        print('Ok! Bye Bye!')


play_game()
   



    