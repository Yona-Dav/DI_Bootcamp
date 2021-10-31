class MenuManager:
    def __init__(self, menu):
        self.menu = menu

    def add_item(self, name, price, spice, gluten):
        new_items = {
        'name': name,
        'price': price,
        'spice level':spice,
        'gluten': gluten
        }
        self.menu.append(new_items)
        return self.menu

    def update_item(self, name, price, spice, gluten):
        item = {
        'name': name,
        'price': price,
        'spice level':spice,
        'gluten': gluten
        }
        # if we want to change the info
        # for dish in self.menu:
        #     if item['name'] == dish['name']:
        #         self.menu.remove(dish)
        #         self.menu.append(item)     
        #         return self.menu
        for dish in self.menu:
            if item['name'] == dish['name']:
                return item
        else:
            return 'Sorry, The dish is not in the menu'
    
    def remove_item(self,name):
        for dish in self.menu:
            if name == dish['name']:
                self.menu.remove(dish)
                print(self.menu)
                break
        else:
            print('The dish is not in the menu')


    

menu_list = [{
    'name': 'Soup',
    'price': 10,
    'spice level':'B',
    'gluten': False
},
{
    'name': "Hamburger",
    'price':15,
    'spice level':'A',
    'gluten': True
},
{
    'name': 'Salad',
    'price':18,
    'spice level':'A',
    'gluten': False
},
{
    'name': 'French Fries',
    'price':5,
    'spice level':'C',
    'gluten': False
},
{
    'name': 'Beef Bourguignon',
    'price': 25,
    'spice level': 'B',
    'gluten': True
}]

current_menu = MenuManager(menu_list)
print(current_menu.add_item('Chicken',12,'B', True))
print(current_menu.update_item('French Fries',5,'C',False))
current_menu.remove_item('Salad')



