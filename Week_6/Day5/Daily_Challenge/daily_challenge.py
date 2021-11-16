import requests
import json
import random
import psycopg2
from tabulate import tabulate


# HOSTNAME = 'localhost'
# USERNAME = 'postgres'
# PASSWORD = 'yoshir34'
# DATABASE = 'countries'
# connect = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
# cursor = connect.cursor()


# cursor.execute('''CREATE TABLE countries
#          (ID serial PRIMARY KEY     NOT NULL,
#          name   varchar(50)   NOT NULL,
#          capital         varchar(50) ,
#          flag text,
#          subregion varchar(255),
#          population bigint );''')

# connect.commit()
# connect.close()

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'yoshir34'
DATABASE = 'countries'

def get_ten_countries():
    url = 'https://restcountries.com/v3.1/all'
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        for i in range(10):
            x = random.randint(0,len(data))
            print(x)
            name = data[x]['name']['common']
            capital = str(data[x]['capital'][0])
            flag = data[x]['flag']
            subregion = data[x].get('subregion', 'no subregion')
            population = data[x]['population']

            connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
            cursor = connection.cursor()
            query = f"INSERT INTO countries (name, capital, flag, subregion, population) VALUES ('{name}','{capital}','{flag}','{subregion}','{population}');"
            cursor.execute(query)
            connection.commit()
            connection.close()
        

    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    cursor = connection.cursor()
    cursor.execute("select * from countries")
    connection.commit()
    results = cursor.fetchall()
    print(tabulate(results, headers=['Name','Capital', 'Flag','Subregion', 'Population']))

get_ten_countries()