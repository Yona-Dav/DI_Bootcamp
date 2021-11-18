# WITH DICTIONARY

users_info = {
    "leo_d": "1234",
    "alex_32":"5895",
    "sarah_v": "9005"
}

# logged_in = []
# while True:
#     user_request = input('Enter login or exit ')

#     if user_request == "exit":
#         break
#     elif user_request=='login':
#         username =input('Enter your username')
#         password = input("Enter your password")
#         if username in users_info.keys() and users_info[username]==password:
#             print('you are now logged in')
#             logged_in.append(username)
#         else:
#             signup = input('Would you like to sign up? ')
#             if signup == 'no':
#                 break
#             else:
#                 username =input('Enter your username')
#                 while username in users_info:
#                     username=input('Enter your username')
#                 password =input("Enter your password")
#                 users_info[username]=[password]

# print(users_info)

# WITH DATABASE

import psycopg2
from tabulate import tabulate

# Create a new table in pgAdmin

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'yoshir34'
DATABASE = 'authentification'
# connect = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
# cursor = connect.cursor()

# cursor.execute('''CREATE TABLE authentification
#          (ID serial PRIMARY KEY     NOT NULL,
#          username   varchar(50)   NOT NULL,
#          password   varchar(30)     NOT NULL);''')

# cursor.execute("insert into authentification(username, password) values ('Lea', '1234') ")
# cursor.execute("insert into authentification(username, password) values ('Sarah', 'hey34') ")
# cursor.execute("insert into authentification(username, password) values ('Bob', 'game27') ")

# connect.commit()
# connect.close()


logged_in = []
while True:
    user_request = input('Enter login or exit ')
    if user_request == "exit":
        break
    elif user_request=='login':
        username = input('Enter your username ')
        password = input("Enter your password ")
        connect = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connect.cursor()
        cursor.execute(f"(select * from authentification where username ='{username}' and password='{password}')")
        user = cursor.fetchall()
        connect.close()
        if len(user) != 0:
            print('you are now logged in')
            logged_in.append(username)
        else:
            signup = input('Would you like to sign up? ')
            if signup == 'no':
                break
            else:
                username =input('Enter your username ')
                connect = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
                cursor = connect.cursor()
                cursor.execute(f"(select username from authentification where username ='{username}')")
                name = cursor.fetchall()
                connect.close()
                while len(name) != 0:
                    username=input('Enter your username ')
                    connect = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
                    cursor = connect.cursor()
                    cursor.execute(f"(select username from authentification where username ='{username}')")
                    name = cursor.fetchall()
                    connect.close()
                password =input("Enter your password ")
                connect = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
                cursor = connect.cursor()
                cursor.execute(f"insert into authentification(username, password) values ('{username}', '{password}') ")
                connect.commit()
                connect.close()


# To have a 'list' of username that exits in the database
def see_users():
    connect = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    cursor = connect.cursor()
    cursor.execute("select username from authentification ")
    connect.commit()
    users = cursor.fetchall()
    connect.close()
    print(tabulate(users, headers=['Username']))

see_users()



### Bonus 

#Example of encrypt/decrypt

from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
f = Fernet(key)
# password = 'hello'
# token = f.encrypt(password.encode())
# print(token)
# decrypt_token = f.decrypt(token)
# print(decrypt_token)

