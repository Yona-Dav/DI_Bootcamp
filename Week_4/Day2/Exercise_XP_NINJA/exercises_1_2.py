# # Exercise 1: Formula
# C = 50
# H = 30
# D = input('Numbers')
# D_split= D.split(',')
# list_number = []

# for i in D_split:
#     list_number.append(int(i))

# print(list_number)

# output = []
# for i in list_number:
#     Q = int(((2*C*i)/H)**(1/2))
#     output.append(Q)

# print(output)


# Exercise 2 : List Of Integers

list_int = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
print(list_int)
list_sorted = sorted(list_int , reverse=True)
print(list_sorted)
print(sum(list_int))

list2 = list_sorted[0] + list_sorted[-1] #A list containing the first and the last numbers.
print(list2)

list_50 = [] #A list of all the numbers greater than 50.
for i in list_sorted:
    if i>50:
        list_50.append(i)
print(list_50)

list_10 = [] # A list of all the numbers smaller than 10.
for i in list_sorted:
    if i<10:
        list_10.append(i)
print(list_10)

list_square = [] #A list of all the numbers squared
for i in list_sorted:
    list_square.append(i*i)
print(list_square)

list_noduplicate = set(list_sorted) #The numbers without any duplicates
print(len(list_noduplicate))

average_num = sum(list_sorted)/len(list_sorted)
print(average_num)

print(max(list_sorted))
print(min(list_sorted))

###BONUS###
# Sum 
sum = 0
for i in list_sorted:
    sum +=i
print(sum)

#average 
average = sum / len(list_sorted)
print(average)

#largest
largest_num = int()
for i in list_sorted:
    if i > largest_num:
        largest_num = i
print(largest_num)

#smallest
smallest_num = int()
for i in list_sorted:
    if i<smallest_num:
        smallest_num = i
print(smallest_num)

### EXTRA BONUS ###
count = 0
number_list = []
while count<10:
    numbers = int(input('Enter a number between -100 and 100'))
    number_list.append(numbers)
    count +=1

print(number_list)