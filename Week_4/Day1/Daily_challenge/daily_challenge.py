# Using the input function, ask the user for a string. The string must be 10 characters long.
sentence = input('Enter a sentence of 10 characters')
if len(sentence)>10:
    print('string not long enough')
elif len(sentence)<10:
    print('string too long')

# print the first and last characters of the given text.
print( f"the first character is {sentence[0]} and the last character is {sentence[len(sentence)-1]}")

# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed.
for i in range(len(sentence)+1):
    print(sentence[:i])

# Swap some characters around then print the newly jumbled string
import random
new_sentence = ''.join(random.sample(sentence, len(sentence)))
print(new_sentence)