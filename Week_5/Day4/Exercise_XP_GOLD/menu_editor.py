from menu_manager import MenuManager

def load_manager():
    new_menu = MenuManager()
    return new_menu

def show_user_menu():
    print('''
    Menu
    1. Add an item
    2. Delete an item
    3. View the menu
    4. Exit''')
    ans = input('Enter your selection ')
    if ans =='1':
        return add_item_to_menu()
    elif ans =='2':
        return remove_item_from_menu()
    elif ans=='3':
        return show_restaurant_menu()
    elif ans=='4':
        x.save_to_file()
        print('The menu was saved')
        return
    else:
        print("I did not understand you answer")
        return show_user_menu()

def add_item_to_menu():
    name = input('Enter the name of the dish ')
    price = int(input('Enter the price of the dish '))
    x.add_item(name,price)
    print('item was added successfully')
    return show_user_menu()

def remove_item_from_menu():
    name = input('Enter the name of the dish ')
    remove = x.remove_item(name)
    print(remove)
    if remove == True:
        print('item was deleted')
    else:
        print("error")
    return show_user_menu()

def show_restaurant_menu():
    print(x.menu)
    return show_user_menu()
    
x=load_manager()    
show_user_menu()
