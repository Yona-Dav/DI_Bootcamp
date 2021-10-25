# Exercise 1 : Favorite Numbers

my_fav_numbers = {3,27,26,51,20}
my_fav_numbers.add(1)
my_fav_numbers.add(7)

friend_fav_numbers = {2,6,9}
our_fav_numbers = friend_fav_numbers | my_fav_numbers
print(our_fav_numbers)

# Exercise 2: Tuple
# Given a tuple which value is integers, is it possible to add more integers to the tuple? NO WE CANNOT CHANGE A TUPLE

# Exercise 3: Print A Range Of Numbers
for i in range(1,21):
    print(i)

# Exercise 4: Floats
# a float is a number with decimal and int is without decimal
# float()

my_list = []
start = 1
while start < 5:
    start += 0.5
    my_list.append(start)
print(my_list)


# Exercise 5: Shopping List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove('Banana') #Remove “Banana” from the list.
basket.remove('Blueberries') #Remove “Blueberries” from the list.
basket.append('Kiwi') #Add “Kiwi” to the end of the list.
basket.insert(0,'Apples') #Add “Apples” to the beginning of the list.

# Count how many apples are in the basket.
count = 0
for fruits in basket:
    if fruits == 'Apples':
        count += 1
print(count)

basket.clear() #Empty the basket.
print(basket)


# Exercise 6 : Loop

# wrong_name = True
# while wrong_name:
#     name = input("Enter a name")
#     if name == "Yona":
#         wrong_name=False
#     else:
#         print('Try again')
# print('You find my name')


# Exercise 7
my_list2 = list(range(0,20,2))
print(my_list2)
for i in my_list2:
    if my_list2.index(i)%2==0:
        print(i)

# Exercise 8
for i in list(range(1500,2501)):
    if i%5==0 and i%7==0:
        print(i)


# Exercise 9: Favorite Fruits
fruits = input('Enter your favorite fruit(s) separate with single space')

s_fruits = fruits.split(' ') #Store the favorite fruit(s) in a list 
print(s_fruits)

name_fruit = input('Enter name of a fruit')

if name_fruit in fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print("You chose a new fruit. I hope you enjoy")


# Exercise 10: Who Ordered A Pizza ?
toppings = []
while True:
    user_choice = input('Enter a topping, when you want to stop input quit')
    if user_choice== 'quit':
        break
    else:
        toppings.append(user_choice)

print(toppings)
price = len(toppings)*2.5+10
print(f"The price of the pizza is: {price}")


# Exercise 11: Cinemax

price = 0
while True:
    age = input('Enter your age and when it finish input quit')
    if age == 'quit':
        break
    elif 2<int(age)<13:
        price+=10
    elif int(age)>12:
        price+= 15
    elif int(age) <3:
        price +=0
print(price)


teens_allowed=[]
while True:
    age = input('Enter your age and when it finish input quit')
    if age == 'quit':
        break
    elif 15<int(age)<22:
        name = input('Enter your name')
        teens_allowed.append(name)
    else:
        print('You can\'t see the moovie')
print(teens_allowed)


# Exercise 12 : Who Is Under 16?
name_list = ['lea', 'tom','sarah', 'shana','mickael','sam']
name_under = []
for i in name_list:
    age = input("Enter your age")
    if int(age) <16:
        name_under.append(i)

for j in name_under:
    name_list.remove(j)


print(name_list)



# Exercise 13
sandwich_orders = ['american', 'kebab','burger']
finished_sandwiches=[]

for i in sandwich_orders:
    print(f'I made you {i} sandwich')
    finished_sandwiches.append(i)

print(finished_sandwiches)


# Exercise 14
sandwich_orders = ['american', 'kebab','burger']
finished_sandwiches=[]
pastrami_order = ['pastrami','pastrami','pastrami']
sandwich_orders+=pastrami_order
print(sandwich_orders)

for i in sandwich_orders:
    if i== 'pastrami':
        print('the deli has run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

for i in sandwich_orders:
    print(f'I made you {i} sandwich')
    finished_sandwiches.append(i)

print(finished_sandwiches)


