# Exercise 1 : Hello World-I Love Python
print( ("Hello world \n")*4 + ('I love python \n')*4)

# Exercise 2 : What Is The Season ?
month = int(input('Enter a month between 1 to 12'))
if 2<month<6:
    print('Spring')
elif 5<month<9:
    print("Summer")
elif 8<month<11:
    print('Autumn')
else:
    print('Winter')
