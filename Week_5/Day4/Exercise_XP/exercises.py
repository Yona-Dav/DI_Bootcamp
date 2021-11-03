# Exercise 1 – Random Sentence Generator
import random
word_list = []

def main():
    print('This is a random sentence generator. We will ask you how long the sentence should be and then priting the generated sentence.In order to print this sentence, a word_list is used. Each word is pick of this list. The sentence do not have to make sense')

def get_words_from_file():
    for word in open('C:/Users/yonab/OneDrive/Bureau/DI_Bootcamp/Week_5/Day4/Exercise_XP/words_list.txt','r'):
        word_list.append(word[:-1])
    print(len(word_list))

get_words_from_file()

def get_random_sentence(length):
    sentence = ''
    for i in range(length):
        sentence += random.choice(word_list).lower()+" "
    print(sentence)  


def validate():
    main()
    length = input('Enter a number between 2 and 20 ')
    if length.isdigit() == False:
        print('It has to be a number ')
        return
    elif int(length)>20 or int(length)<2:
        print('The length has to be between 2 and 20')
        return 
    else:
        return get_random_sentence(int(length))

# validate()




# Exercise 2: Working With JSON
import json

with open('C:/Users/yonab/OneDrive/Bureau/DI_Bootcamp/Week_5/Day4/Exercise_XP/file.json','r') as f:
    sample = json.load(f)

print(next(iter(sample['company']['employee']['payable'])))

sample['company']['employee']['birth_date'] = 'January'
print(sample['company']['employee'])
with open('C:/Users/yonab/OneDrive/Bureau/DI_Bootcamp/Week_5/Day4/Exercise_XP/file.json', 'w') as f:
    json.dump(sample, f, indent=2)


