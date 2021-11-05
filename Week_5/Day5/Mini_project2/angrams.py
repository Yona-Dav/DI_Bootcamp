from anagram_checker import AnagramChecker

def is_word_valid(word):
    return len(word.split())==1 and word.isalpha()


while True:
    print('''
    Menu
    1.Find a word\'s anagrams
    2. Exit''')
    user_choice = input('Enter your option ')
    if user_choice == '2':
        print('Goodbye')
        break
    elif user_choice == '1':
        selected_word = input('Enter a word to check for anagram(s) ')
        if is_word_valid(selected_word):
            clean_word = selected_word.strip()
            a = AnagramChecker()
            anagrams = a.get_anagrams(clean_word)
            msg = f'''
            You word :{clean_word}
            this is a valid English word
            Anagram for you word:'''
            print(msg, *anagrams)
        else:
            print('not a valid word')
        
