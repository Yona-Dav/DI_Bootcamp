# Exercise 1: Birthday Look-Up + # Exercise 2: Birthdays Advanced + #Exercise 3: Add Your Own Birthday
birthdays={
    'Lea': '2000/12/24',
    'Sarah':'1985/03/12',
    'Moshe': '2004/08/05',
    'Tom':' 1975/05/31',
    'Adam': '1999/09/09',
}

print("Welcome User! You can look up the birthdays of the people in the list!")

# your_name = input('Enter your name')
# bday = input(f"Hi {your_name}, what is you birthday (format YYYY/MM/DD)")

# birthdays[your_name]=bday

# print(birthdays.keys())
# person = input('Enter a person\'s name from the list')
# while person not in birthdays.keys():
#     print(f'Sorry, we don’t have the birthday information for {person}')
#     person = input('Enter a person\'s name from the list')
# print(f'The birthday of {person} is {birthdays[person]}')


#Exercise 4: Fruit Shop

items = {
    'banana':4,
    'apple':2,
    'orange': 1.5,
    'pear': 3
}

for k,v in items.items():
    print(f'The price of {k} is ${v}')

amount = [2,7,5,9]
for k,v,i in zip(items.keys(),items.values(),amount):
    items[k] = {'price': v ,'item_amount':i}

print(items)

total_cost = 0
for keys in items:
    total_cost += items[keys]['price']*items[keys]['item_amount']
print(total_cost)



# Exercise 5 : Cars

car_brand = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
car_brand_list = car_brand.split(', ') #Convert it into a list using Python
print(car_brand_list)

print(f'There are {len(car_brand_list)} companies in the list') #how many manufacturers/companies are in the list.

print(sorted(car_brand_list, reverse=True)) #list of manufacturers in reverse/descending order (Z-A).

list_with_o = []
list_with_o = [ x for x in car_brand_list if 'o' in x]
print(len(list_with_o)) # how many manufacturers’ names have the letter ‘o’ in them.

list_without_i = []
list_without_i = [ x for x in car_brand_list if 'i' not in x]
print(len(list_without_i)) # how many manufacturers’ names do not have the letter ‘i’ in them.

new_list = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
new_list = set(new_list)
new_list =list(new_list)

new_str = ','.join(new_list)
print(new_str)

print(f'There are {len(new_list)} companies')

# list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.
new_list_sorted = sorted(new_list)
for i in range(0,len(new_list_sorted)):
    new_list_sorted[i] = new_list_sorted[i][::-1]
print(new_list_sorted)




