class AnagramChecker:
    '''
    The AnagramChecker program asks the user for a word.
    It checks if the word is a valid English word, and then finds all possible anagrams for that word.'''

    def __init__(self, file_name='C:/Users/yonab/OneDrive/Bureau/DI_Bootcamp/Week_5/Day4/Exercise_XP/words_list.txt'):
        with open(file_name) as f:
            self.words = [word.strip().upper() for word in f.readlines()] #with the upper, I make sure that all the word uppercase
            # self.words = list(map(lambda x:x.strip(), f.readlines)) # Other way

    def is_valid_word(self,word):
        return word.upper() in self.words # return True or False

    def get_anagrams(self,word):
        word_sorted = sorted(list(word.upper())) #We have to put in a list because we cannot sort a string directly ]
        anagrams=[]
        for other_word in self.words:
            if sorted(list(other_word))==word_sorted:
                anagrams.append(other_word)
        anagrams.remove(word.upper())
        return anagrams
