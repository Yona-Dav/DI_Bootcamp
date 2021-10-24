# Exercise 1 : Hello World
print(('Hello world \n')*4)

# Exercise 2 : Some Math
res = (99^3) * 8
print(res)

# Exercise 3 : What Is The Output ?
# >>> 5 < 3 false
# >>> 3 == 3 true
# >>> 3 == "3" false
# >>> "3" > 3 error 
# >>> "Hello" == "hello" false

# Exercise 4 : Your Computer Brand
# Create a variable called computer_brand which value is the brand name of your computer.
computer_brand = 'Dell'
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
print(f'I have a {computer_brand} computer')

# Exercise 5 : Your Information
name = 'Yona'
age = 27
shoe_size = 37
sentence = 'My name is {} and I am {}. If you want to buy me shoes, my shoe size is {}'.format(name, age, shoe_size)
print(sentence)

# Exercise 6 : A & B
a = 5
b = 4
if a>b:
    print('Hello world')

# Exercise 7 : Odd Or Even
number = int(input("Enter a number"))
if number%2 == 0:
    print('This number is even')
else:
    print('This number is odd')

# Exercise 8 : What’s Your Name ?
name_user = input('Enter you name').lower()

if  name_user == 'yona':
    print('You have a very beautiful name ')
else:
    print('My name is more beautiful')


# Exercise 9 : Tall Enough To Ride A Roller Coaster

height_inches = int(input('Enter you height in inches'))
height_cm = height_inches * 2.54
if height_cm > 145:
    print('You are tall enough to ride')
else:
    print('You need to grow some more to ride')


# Write a code that receives 3 inputs and combines them:
# A number input (integer, float etc.)
# A number input (integer, float etc.)
# A string, describing an operator (“add”, “multiply”, “divide”)
# If the first two inputs are equal -> print number1 with the power of number2.
# Otherwise, perform the 3rd input’s operator on number1 with number2 and print the result.
# If the input from the user isn’t correct -> print an error message.

while True:
    try:
        num_one = int(input('Enter a number'))
        num_two = int(input('Enter a number'))
        operator = input('Choose an operator: +, * or /')
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if num_one == num_two: 
        x = num_one**num_two
        print(x)
    else:
        if operator == '+':
            print(num_one+num_two)
        elif operator == '*':
            print(num_two*num_one)
        elif operator == '/':
            print(num_one/num_two)
        
            

