# Perfect Number
# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

number = int(input('Enter a number'))

sum_divisors = 0
list_divisors = []
for i in range(1,number):
    if number%i==0:
        sum_divisors += i
        list_divisors.append(i)

if sum_divisors == number:
    print(True)
else:
    print(False)

print(list_divisors)