# Exercise 3 : Outputs
# Predict the output of the following code snippets:
#     >>> 3 <= 3 < 9 true
#     >>> 3 == 3 == 3 true
#     >>> bool(0) false
#     >>> bool(5 == "5") false
#     >>> bool(4 == 4) == bool("4" == "4") true
#     >>> bool(bool(None)) false

# x = (1 == True) 
# y = (1 == False) 
# a = True + 4
# b = False + 10

# print("x is", x)  true
# print("y is", y) false
# print("a:", a)  5
# print("b:", b)  10

# Exercise 4 : How Many Characters In A Sentence ?

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.Excepteur sint occaecat cupidatat non proident,sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))


# Exercise 5: Longest Word Without A Specific Character
# Keep asking the user to input the longest sentence they can without the character “A”.
# # Each time a user successfully sets a new longest sentence, print a congratulations message.

longest_sent = ''
while True:
    sent = input('Enter a sentence without a')
    if len(sent)>len(longest_sent):
        longest_sent=sent
        print("Congratulation !You find a new longest sentence")
    else:
        print('It is shorter than the longest sentence ')
 