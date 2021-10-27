# Exercise 1: Temperature Advice

import random 

# def get_random_temp():
#     number = random.randint(-10,40)
#     return number

# def main():
#     temp = get_random_temp()
#     return (f'The temperature right now is {temp} degrees Celsius.')


# def main():
#     temp = get_random_temp()
#     if temp < 0:
#         return ('Brrr, that’s freezing! Wear some extra layers today')
#     elif 0<=temp<16:
#         return ('Quite chilly! Don’t forget your coat')
#     elif 15<temp<24:
#         return('Yeah! You can go to the park')
#     elif 23<temp<33:
#         return('Lets go to the swimming pool!')
#     else:
#         return ('You need air conditionner ')



# def get_random_temp(season):
#     if season == 'winter':
#         number = random.randint(-10,16)
#         return number
#     elif season == 'summer':
#         number = random.randint(28,40)
#         return number
#     elif season == "autumn":
#         number = random.randint(12,20)
#         return number
#     elif season == 'spring':
#         number = random.randint(16,30)
#         return number
#     else:
#         return 'It is not a season'

# def main(season):
#     temp = get_random_temp(season)
#     if temp < 0:
#         return ('Brrr, that’s freezing! Wear some extra layers today')
#     elif 0<=temp<16:
#         return ('Quite chilly! Don’t forget your coat')
#     elif 15<temp<24:
#         return('Yeah! You can go to the park')
#     elif 23<temp<33:
#         return('Lets go to the swimming pool!')
#     else:
#         return ('You need air conditionner ')

# print(main('winter'))


### BONUS ###
# def get_random_temp():
#     number = round(random.uniform(-10, 40), 2)
#     return number
# print(get_random_temp())


####BONUS####

def get_random_temp(month):
    if int(month)==12 or int(month)==1 or int(month)==2:
        number = random.randint(-10,16)
        return float(number)
    elif int(month) == 3 or int(month)==4 or int(month)==5:
        number = random.randint(16,30)
        return float(number)
    elif int(month) == 7 or int(month)==8 or int(month)==6 or int(month)==2:
        number = random.randint(28,40)
        return float(number)
    elif int(month) == 9 or int(month)==10 or int(month)==11:
        number = random.randint(12,20)
        return float(number)

def main(month):
    temp = get_random_temp(month)
    print(temp)
    if float(temp) < 0:
        return ('Brrr, that’s freezing! Wear some extra layers today')
    elif 0<=float(temp)<16:
        return ('Quite chilly! Don’t forget your coat')
    elif 15<float(temp)<24:
        return('Yeah! You can go to the park')
    elif 23<float(temp)<33:
        return('Lets go to the swimming pool!')
    else:
        return ('You need air conditionner ')

print(main(10))
