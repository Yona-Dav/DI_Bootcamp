# Exercise 1: List Of Integers - Randoms

import random
from random import randint
# for 10 integers
# for i in range(10):
# 	value = randint(-100, 100)
# 	print(value)

# For random positive integer
numbers = []
for i in range(randint(50,100)):
	value = randint(-100, 100)
	numbers.append(value)

print(numbers)
print(len(numbers))

# Exercise 2: Authentication CLI - Login & Exercise 3: Authentication CLI - Signup:

users_info = {
    "leo_d": "1234",
    "alex_32":"5895",
    "sarah_v": "9005"
}

logged_in = []
while True:
    user_request = input('Enter login or exit')

    if user_request == "exit":
        break
    elif user_request=='login':
        username =input('Enter your username')
        password = input("Enter your password")
        if username in users_info.keys() and users_info[username]==password:
            print('you are now logged in')
            logged_in.append(username)
        else:
            signup = input('Would you like to sign up? ')
            if signup == 'no':
                break
            else:
                username =input('Enter your username')
                while username in users_info:
                    username=input('Enter your username')
                password =input("Enter your password")
                users_info[username]=[password]

print(users_info)



