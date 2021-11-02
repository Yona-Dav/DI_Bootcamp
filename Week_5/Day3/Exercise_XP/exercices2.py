# Exercise 1

import datetime
def date_of_today():
    return datetime.date.today()

print(date_of_today())

# Exercise 2
def amount_time():
    jan = datetime.datetime(2022,1,1)
    actual_datetime = datetime.datetime.now()

    time_left = jan - actual_datetime
    return f'the 1st of January is in {time_left}hours'

print(amount_time())

# Exercise 3

def minute_alive(birthdate):
    bday = datetime.datetime.strptime(birthdate, "%d/%M/%Y")
    today = datetime.datetime.now()
    time_alive = today - bday
    return f'Minutes your has been alive until now : {time_alive.total_seconds()/60}'

print(minute_alive('27/03/1994'))


# Exercise 4

def next_holidays():
    dtoday = datetime.datetime.now()
    print(dtoday)
    holidays = {'Hanouka': '30/11/2021', 'Pourim':"16/03/2022", 'Pessah': "07/04/2022"}
    next_holiday = datetime.timedelta(days=365, seconds=0, microseconds=0)
    Theholiday = ''
    for holiday, date in holidays.items():
        h_date = datetime.datetime.strptime(date, "%d/%m/%Y")
        time_left = h_date-dtoday
        if time_left<next_holiday:
            next_holiday = time_left
            Theholiday = holiday

    print(f'The next holiday is {Theholiday} and this is in  {next_holiday}')

next_holidays()

# Exercise 5 : How Old Are You On Jupiter?
sec = 31557600
planets = {'Earth': 1 , 'Mercury':0.2408467,'Venus':0.61519726,'Mars':1.8808158,"Jupiter":11.862615,'Saturn':29.447498,'Uranus':84.016846,'Neptune':164.79132}
def how_old(age):
    for planet, years in planets.items():
        print(f'You are {age/(sec*years)} Earth-years old on {planet}')

how_old(1000000000)

# Exercise 6 : Faker Module
from faker import Faker
fake = Faker()
users = []
def add_users():
    info_user={
        'name': fake.name(),
        'adress':fake.address(),
        'language_code':fake.language_code()
    }
    users.append(info_user)
    print(users)

add_users()
add_users()
add_users()

