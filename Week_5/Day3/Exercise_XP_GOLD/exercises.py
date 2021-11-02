# Exercise 1 : Regular Expression #1

import re
def return_numbers(string):
    number = re.findall('[0-9]',string)
    for i in number:
        print(i,end='')
    print('')

return_numbers('k5k3q2g5z6x9bn') 


# Exercise 2 : Regular Expression #2
def validity_name():
    full_name = input('Enter your full name ')

    if len(re.findall('[0-9]',full_name ))>0:
        print('The name should contain only letters.')
        return validity_name()
    elif len(re.findall('[ ]',full_name))>1:
        print('The name should contain only one space.')
        return validity_name()
    elif (full_name.title()) != full_name:
        print('The first letter of each name should be upper cased')
        return validity_name()

#print(validity_name())

# Exercise 3: Python Password Generator

class Password:
    def __init__(self):
        pass

    def check_validity(self):
        password = input('Enter your password ')
        if re.search('[0-9]', password)==None:
            print('Password has to contain at least 1 digit')
            return self.check_validity()
        elif len(password)<6 or len(password)>30:
            print('Length of the password has to be between 6 and 30 characters')
            return self.check_validity()
        elif re.search('[a-z]', password)==None:
            print('Password has to contain at least 1 lower-case character')
            return self.check_validity()
        elif re.search('[A-Z]', password)==None:
            print('Password has to contain at least 1 upper-case character')
            return self.check_validity()
        elif re.search("[$&+,:;=?@#|'<>.^*()%!-]", password)==None:
            print('Password has to contain at least 1 special character')
            return self.check_validity()
        else:
            print(f'Your password is {password}, keep it in a safe place!')
        
        
new = Password()
new.check_validity()
