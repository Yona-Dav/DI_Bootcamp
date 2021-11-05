# Part 1 : Quizz :
# Answer the following questions

# What is a class?A class is a code template for creating objects. Objects have member variables and have behaviour associated with them.

# What is an instance? An object is created using the constructor of the class. This object will then be called the instance of the class.

# What is encapsulation? We can restrict access to methods and variables. This prevents data from direct modification, which is called encapsulation.

# What is inheritance? Inheritance is the process by which one class takes on the attributes and methods of another.

# What is multiple inheritance? A class can inherit from two different classes; in this case, the order of the parent class in a class definition will decide what will be inherited

# What is polymorphism? Polymorphism allows the ability to use a standard interface for multiple forms or data types.

# What is method resolution order or MRO? Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute.

# Part 2: Create A Deck Of Cards Class.
import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} {self.suit}'

class Deck(Card):
    def __init__(self):
        self.cards = []
        self.__game()
        print(self.cards)

    def __game(self):
        for i in ['Hearts','Diamonds','Clubs','Spades']:
            for j in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
                self.cards.append(Card(i,j))
    
    def shuffle(self):
        if len(set(self.cards))==52:
            random.shuffle(self.cards)
            return 'The card game deck was shuffled'
        else:
            raise Exception('The number of card is not 52 ')

    def deal(self):
        if len(self.cards)>0:
            x = self.cards.pop()
            return f'The draw card is {x}'
        else:
            return 'The card game deck is empty'

    
test = Deck()
print(test.shuffle())
print(test.deal())