# Exercise 1 : Restaurant Menu Manager
import json

class MenuManager:
    def __init__(self):
        with open('C:/Users/yonab/OneDrive/Bureau/DI_Bootcamp/Week_5/Day4/Exercise_XP_GOLD/menu.json','r') as f:
            self.menu = json.load(f)

    def add_item(self,name,price):
        item = {
            'name': name,
            'price': price
        }
        self.menu['items'].append(item)
    
    def remove_item(self,name):
        for i in self.menu['items']:
            if i['name']==name:
                self.menu['items'].remove(i)
                return True    
        return False

    def save_to_file(self):
        with open('C:/Users/yonab/OneDrive/Bureau/DI_Bootcamp/Week_5/Day4/Exercise_XP_GOLD/menu.json', 'w') as f:
            json.dump(self.menu, f, indent=2)

test = MenuManager()
print(test.remove_item("Salad"))  


# with open('C:/Users/yonab/OneDrive/Bureau/DI_Bootcamp/Week_5/Day4/Exercise_XP_GOLD/menu.json','r') as f:
#     menu = json.load(f)
# def remove(name):
#     for i in menu['items']:
#         if i['name']==name:
#             menu['items'].remove(i)
#             return True
#     return False

# print(remove('Sala'))