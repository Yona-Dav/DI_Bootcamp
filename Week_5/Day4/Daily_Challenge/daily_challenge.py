import string 
import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')
import re

class Text:
    def __init__(self,text):
        self.string = text
        self.text = text.lower().split(' ')
        self.freq = {}
        for text in self.text:
            if text in self.freq:
                self.freq[text]+=1
            else:
                self.freq[text]=1
        
    
    def word_frequency(self,word):
        for k,v in self.freq.items():
            if word == k:
                return f'The word {word} is used {v} times in the text'
        return f'The word {word} is not in the text'
    
    def most_common(self):
        sorted_dict = dict(sorted(self.freq.items(), key=lambda item: item[1], reverse=True))
        return f'The most common word in the text is: {next(iter(sorted_dict))}' 

    def uniq_word(self):
        uniq = []
        for keys in self.freq:
            uniq.append(keys)
        return uniq
    
    @classmethod
    def from_file(cls,file):
        with open(file,'r') as f:
            text = f.read()
        return cls(text)
        
class TextModification(Text):
    def __init__(self,text):
        super().__init__(text)
    
    def without_punctuation(self):
        return self.string.translate(str.maketrans('', '', string.punctuation))
    
    def without_stopwords(self):
        text_without = [word for word in self.text if not word in stopwords.words()]
        return ' '.join(text_without)

    def without_special_char(self):
        my_new_text = re.sub("[$&+=@#|'<>.^*()%-]", '', self.string)
        return my_new_text

    


# text = TextModification('this is// the first@ time , this is incredible , this show')
# print(text.without_punctuation())
# text.without_stopwords()
# print(text.without_special_char())
# print(text.most_common())
# print(text.uniq_word())
# print(text.word_frequency('this'))

text2 = Text.from_file('C:/Users/yonab/OneDrive/Bureau/DI_Bootcamp/Week_5/Day4/Daily_Challenge/the_stranger.txt')
print(text2.word_frequency('coming'))
print(text2.most_common())