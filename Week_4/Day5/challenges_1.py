#Exercise 1
#Write a script that inserts an item at a defined index in a list.

list = [1,2,3,4]
list.insert(2,62) # in index2
print(list)

#Exercise 2
# Write a script that counts the number of spaces in a string

sentence = "This is a Beautiful Day"
print(sentence.count(' '))

# Exercise 3
# Write a script that calculates the number of upper case letters and lower case letters in a string.
import string
upper_letter = string.ascii_uppercase
lower_letter = string.ascii_lowercase
count_upper = 0
count_lower = 0
for l in sentence:
    if l in upper_letter:
        count_upper += 1
    elif l in lower_letter:
        count_lower +=1
print(f'Number of upper case letter : {count_upper} \nNumber of lower case letter: {count_lower}')

# Exercise 4
# Write a function to find the sum of an array without using the built in function:

numbers = [1,5,4,2]
def summ(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(summ(numbers))

# Exercise 5
# Write a function to find the max number in a list

def max_number(list_number):
    max = int()
    for i in numbers:
        if i>max:
            max = i
    return max
print(max(numbers))

# Exercise 6
# Write a function that returns factorial of a number

def factorial(num):
    count = 1
    for i in range(1,num+1):
        count *=i
    return count
print(factorial(4))


# Exercise 7
# Write a function that counts an element in a list (without using the count method):


def count_element(list_element, element):
    count =0
    for i in list_element:
        if i == element:
            count +=1
    return count

my_list = ['a','a','t','o']
print(count_element(my_list,'a'))

# Exercise 8
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

def norm(list):
    total = 0
    for i in list:
        total += i*i
    return int(total**(1/2))

print(norm([1,2,2]))

# Exercise 9
# Write a function to find if an array is monotonic (sorted either ascending of descending)

def is_mono(arr):
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        return True
    else:
        return False

print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))

# Exercise 10
# Write a function that prints the longest word in a list.

def longuest_word(list):
    longuest = ''
    for i in list:
        if len(i)>len(longuest):
            longuest = i
    return longuest

print(longuest_word(['your','computer','javascript','python']))

# Exercise 11
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

mix_list = [1,'you',2,8,956,'hello','world']
int_list = []
str_list = []
for i in range(len(mix_list)):
    if isinstance(mix_list[i],int)==True:
        int_list.append(mix_list[i])
    else:
        str_list.append(mix_list[i])

print(int_list)
print(str_list)


# Exercise 12
# Write a function to check if a string is a palindrome:

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(is_palindrome('radar'))
print(is_palindrome('John'))

# Exercise 13
# Write a function that returns the amount of words in a sentence with length > k:

def sum_over_k(sentence,num):
    count =0
    for word in sentence.split(' '):
        print(word)
        if len(word)>num:
            count+=1
    return count

sentence3 = 'Do or do not there is no try'
print(sum_over_k(sentence3,2))

# Exercise 14
# Write a function that returns the average value in a dictionary (assume the values are numeric):
def average_value(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total/len(dictionary)

print(average_value({'a': 1,'b':2,'c':8,'d': 1}))

# Exercise 15
# Write a function that returns common divisors of 2 numbers:

def common_div(num1,num2):
    div = []
    for i in range(1,num1+1):
        for j in range(1,num2+1):
            if num1%i==0 and num2%j==0 and i==j:
                div.append(i)
    return div

print(common_div(20,10))

# Exercise 16
# Write a function that test if a number is prime:

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

print(is_prime(11))

# Exercise 17
# Write a function that prints elements of a list if the index and the value are even:

def even_index(list):
    even_list=[]
    for i in range(len(list)):
        if i%2==0 and list[i]%2==0:
            even_list.append(list[i])
    return even_list

print(even_index([1,2,2,3,4,5]))

# Exercise 18
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

def type_count(**args):
    count_int = 0
    count_str = 0
    count_float = 0
    count_bool = 0
    for key, value in args.items():
        if isinstance(value, bool)==True:
            count_bool += 1
        elif isinstance(value, int)==True:
            count_int += 1
        elif isinstance(value, str)==True:
            count_str += 1
        elif isinstance(value, float)==True:
            count_float += 1
        
    return f'int:{count_int}, str:{count_str}, float:{count_float}, bool:{count_bool}'

print(type_count(a=1,b='string',c=1.0,d=True,e=False))

# Exercise 19
# Write a function that mimics the builtin .split() method for strings.
sen = 'this is crazy'
my_new_list = []
for i in range(len(sen)):
    if sen[i]==' ':
        my_new_list.append(sen[:i])

def split(sentence, delimiters):
    my_new_list = []
    word=''
    for i in sentence:
        if i not in delimiters:
            word += i
        else:
            my_new_list.append(word)
            word = ''
    my_new_list.append(word)
    return my_new_list

print(split('You are amazing',' '))



# Exercise 20
# Convert a string into password format.

password = 'mypassword'
password_hidden = '*'*len(password)
print(password_hidden)