# Exercise 1 : Box Of Stars


def longuest_words(*args):
    longuest_word = ''
    for arg in args:
        if len(arg)>len(longuest_word):
            longuest_word = arg
    return len(longuest_word)

def box_printer(*args):
    print('*'*2+'*'*longuest_words(*args)+'*'*2)
    for arg in args:
        space = longuest_words(*args) - len(arg)
        print('*'+' '+arg+' '*space+' '+'*')
    print('*'*2+'*'*longuest_words(*args)+'*'*2)

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")


# Exercise 2
'''this algorithm is used to sort'''
def insertion_sort(alist):
   for index in range(1,len(alist)):

    currentvalue = alist[index]
    position = index

    while position>0 and alist[position-1]>currentvalue:
        alist[position]=alist[position-1]
        position = position-1

    alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)