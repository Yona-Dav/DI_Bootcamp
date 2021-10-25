# Exercise 1 : Concatenate Lists
my_list1 = [0,2,4]
my_list2 = [3,7,9]
for i in my_list2:
    my_list1.append(i)
print(my_list1)

# Exercise 2: Greatest Number
number = input("Enter 3 numbers ") 
number = number.split(' ')

num =[]
for i in number:
    i = int(i)
    num.append(i)
print(max(num))


# Exercise 3 : The Alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = ['a','e','i','o','u','y']

for i in alphabet:
    if i in vowels:
        print(i, 'is a vowel')
    else:
        print(i,"is a consonant")



# Exercise 4 :

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

your_name = input("Enter your name")
if your_name in names:
    print(f"{your_name} with the index {names.index(your_name)}")


# Exercise 5 : Words And Letters

words = input('Enter seven words separate with space')
list_word = words.split(' ')

letter = input("Enter a letter")

for i in list_word:
    if letter in i:
        print(f'In {i} the letter {letter} is in index of {i.index(letter)}')
    else:
        print(f'the word {i} and the letter {letter}')


# Exercise 6 :
list_num = list(range(0,1000001))
print(min(list_num))
print(max(list_num))
print(sum(list_num))

# Exercise 7 :

seq_num = input('Enter sequence of comma-separated numbers. ')
list_number = seq_num.split(',')
tuple_number = tuple(list_number)
print(list_number)
print(tuple_number)

# Exercise 8 : Random Number
import random

# random_number = random.randint(1,10)
# print(random_number)

# number1_9 = int(input('Enter a number from 1 to 9 including'))
# if number1_9 == random_number:
#     print('You win')
# else:
#     print("better luck next time")

# Bonus

count_win = 0
count_lost = 0
while True:
    random_number = random.randint(1,10)
    print(random_number)
    number1_9 = input('Enter a number from 1 to 9 including')
    if number1_9 =='quit':
        break
    elif int(number1_9) == random_number:
        print('You win')
        count_win +=1
    else:
        print("better luck next time")
        count_lost +=1

print(count_lost)
print(count_win)