# Exercise 1

# first method
m = 2
for i in range(0, 6, 2):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for k in range(0, i + 1):
        print("*", end='')
    print("")  # need a new line


m = 5
for i in range(0, 6):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for k in range(0, i):
        print("*", end='')
    print("")


m = 0
for i in range(0, 6):
    print('*'*i)
for l in range(5, 0, -1):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m + 1
    for k in range(l, 0, -1):
        print("*", end='')
    print("")

# Second method


def stars_picture(picture):
    for row in picture:
        for pixel in row:
            if pixel == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print('')


triangle = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1]]

triangle2 = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]]


stars_picture(triangle)
stars_picture(triangle2)


# Exercise 2
my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):  # i index from 0 to 4
    minimum = i
    for j in range(i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]):  # find the minimum between two numbers
            minimum = j
            if(minimum != i):
                # the min is the first
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)

# the purpose of this program is to sort the list
