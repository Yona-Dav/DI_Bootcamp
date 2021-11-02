# Exercise 1 : Built-In Functions

class Mathematics:

    def __abs__(self,number):
        '''The abs function return the absolute value'''
        if isinstance(number,int)==False and isinstance(number,float)==False:
            raise Exception("This is not a number!")
        elif isinstance(number,int)==True or isinstance(number,float)==True:
            if number >= 0:
                return number
            else:
                return number*(-1)

    def __int__(self,string):
        ''' The int function is used to convert a string to an integer or to write a number without decimal'''
        return int(string)



    def __input__(self):
        '''The input function allow the user to enter a string in order to use it after (into a program)'''
        test = input("Write what you want")
        return f'You just write {test}'

    

math = Mathematics()
print(math.__abs__(-35))
print(Mathematics.__abs__.__doc__)
print(Mathematics.__int__.__doc__)
print(Mathematics.__input__.__doc__)

# Exercise 2: Currencies

class Currency:
    def __init__(self,currency,amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other,float):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError(f'Cannot add between Currency type {self.currency} and {other.currency}')


    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
            return self
        elif isinstance(other,float):
            self.amount += other
            return self
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
                return self
            else:
                raise TypeError(f'Cannot add between differente Currency ')   
    


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


