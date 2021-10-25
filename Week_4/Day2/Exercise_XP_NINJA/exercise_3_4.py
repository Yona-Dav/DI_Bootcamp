# Exercise 3: Working On A Paragraph
text = "Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming."



print(f'Number of characters : {len(text)}') #How many characters it contains

num_sentence = 0
for i in text:
    if i=='.':
        num_sentence+=1
print(f'Number of sentence: {num_sentence}') #How many sentences it contains.

s_text = text.split(' ')
print(f'Number of words : {len(s_text)}') #How many words it contains.

unique_word = []
for word in s_text:
    if word not in unique_word:
        unique_word.append(word)
print(f'Number of unique words : {len(unique_word)}') #How many unique words it contains.

average_word_sent = len(s_text)/num_sentence
print(f'The average amount of word per sentence : {average_word_sent}')

non_unique = len(s_text)-len(unique_word)
print(f'The number of non unique words : {non_unique}')

list_element = []
for i in text:
    list_element.append(i)

num_whitespace = 0
for i in list_element:
    if i==' ':
        num_whitespace += 1 
print(f'The number of non-whitespace : {len(list_element)-num_whitespace}')


# Exercise 4
# Write a program that prints the frequency of the words from the input.

word_freq = {}
sentence = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'

for word in sentence.split(' '):
    count = 0
    if word not in word_freq.keys():
        count +=1
        word_freq[word]=count
    else:
        word_freq[word] += 1
print(word_freq)
