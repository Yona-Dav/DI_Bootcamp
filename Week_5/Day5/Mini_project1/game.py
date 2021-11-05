import random

class Game:
    user_selected = ''
    computer_select = ''
    results = {'win':0,'loss':0,'draw':0}

    def get_user_item(self):
        while True:
            print('''
            Options:

            r : rock
            p : paper
            s : scissors
            ''')

            self.user_selected = input('Enter your choice ')
            if self.user_selected in 'rR':
                self.user_selected = 'rock'
                return self.user_selected
            elif self.user_selected in 'pP':
                self.user_selected = 'paper'
                return self.user_selected
            elif self.user_selected in 'sS':
                self.user_selected = 'scissors'
                return self.user_selected
            else:
                print('You answer is not valid')
    
    def get_computer_item(self):
        self.computer_select = random.choice(['rock','paper','scissors'])
        return self.computer_select

    def get_game_result(self, user_item, computer_item):
        if user_item == 'rock':
            if computer_item == 'paper':
                self.results['loss'] +=1
                return 'loss'
            elif computer_item =='scissors':
                self.results['win'] +=1
                return 'win'
            else:
                self.results['draw'] +=1
                return 'draw'
        elif user_item=='paper':
            if computer_item == 'paper':
                self.results['draw'] +=1
                return 'draw'
            elif computer_item =='scissors':
                self.results['loss'] +=1
                return 'loss'
            else:
                self.results['win'] +=1
                return 'win'
        else:
            if computer_item == 'paper':
                self.results['win'] +=1
                return 'win'
            elif computer_item =='rock':
                self.results['loss'] +=1
                return 'loss'
            else:
                self.results['draw'] +=1
                return 'draw'
    
    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_item()
        print(f'''
        You selected : {user}
        The computer selected: {computer}
        The result: {self.get_game_result(user,computer)}''')


        