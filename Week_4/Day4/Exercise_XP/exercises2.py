from datetime import date


# Exercise 7: When Will I Retire ?

today_year = date.today().year
today_day = date.today().day
today_month = date.today().month

def get_age(year, month, day):
    age = int()
    if int(month) < today_month:
        age = today_year - int(year)
    elif int(month) == today_month:
        if int(day)<=today_day:
            age = today_year - int(year)
        else:
            age = today_year - int(year) -1
    else:
        age = today_year -1 - int(year)
    return age

# print(get_age(1994,3,27))

def can_retire(gender, date_of_birth):
    age = get_age(date_of_birth[0:4], date_of_birth[5:7],date_of_birth[8:10])
    if gender == 'm' and age>66:
        return True
    elif gender == 'f' and age>61:
        return True
    else:
        return False

# gender = input('What is your genre : m or f')
# date_of_birth = input('Enter your birthday yyyy/mm/dd')
# print(can_retire(gender, date_of_birth))

# Exercise 8:

def calcul(value):
    res = 0
    for i in range(1,5):
        res += int(str(value)*i)
    return res

print(calcul(3))
