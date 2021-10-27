import random

# Exercise 1 : What Are You Learning ?
def display_message():
    print('I am learning how to code')
display_message()

# Exercise 2: What’s Your Favorite Book ?
def favorite_book(title):
    print(f'One of my favorite book is {title}')
favorite_book('Alice in Wonderland')

# Exercise 3 : Some Geography
def describe_city(city, country='France'):
    print(f'{city} is in {country}')
describe_city('Montpellier')

#Exercise 4 : Random
def random_number(number):
    number2 = random.randint(0, 100)
    if number2==number:
        print('Congratulation, You found the number!')
    else:
        print('You failed')
        print(f'Your number was {number} and the computer number was {number2}')
random_number(10)

# Exercise 5 : Let’s Create Some Personalized Shirts !
# def make_shirt(size, message):
#     print(f'The size of the shirt is {size} and the message is {message}')

# make_shirt('L',"Hello")

# def make_shirt(size='L', message='I love Python'):
#     print(f'The size of the shirt is {size} and the message is {message}')

# make_shirt()
# make_shirt("M")
# make_shirt('L',"Hello")

def make_shirt(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
make_shirt(size='L',message="Hello")

# Exercise 6 : Magicians …
magician = ["leo","Tom","Ricky"]

def show_magicians(magician):
    for name in magician:
        print(name)
show_magicians(magician)

def make_great(magician):
    great_magicians = []
    while magician:
        name = magician.pop()
        great_magician = name + ' The great'
        great_magicians.append(great_magician)
    
    for great_magician in great_magicians:
        magician.append(great_magician)
    


make_great(magician)
show_magicians(magician)
