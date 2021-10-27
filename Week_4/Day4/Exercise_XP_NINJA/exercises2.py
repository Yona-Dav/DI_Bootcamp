# Exercise 1 : What’s Your Name ?

def get_full_name(**kargs):
    full_name = ''
    for key,value in kargs.items():
        full_name += value.title()

    return full_name

print(get_full_name(first_name="john ", middle_name="hooker ", last_name="lee ")) 
print(get_full_name(first_name="bruce", last_name="lee"))

# Exercise 2 : From English To Morse
CODE = {' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}

def convert_to_morse(text):
    text = text.upper()
    morse_sentence = ''
    for char in text:
        morse_sentence += CODE[char]+' '
    return morse_sentence

def convert_to_text(code):
    sentence =''
    s_code = code.split(' ')
    for char in s_code:
        for key, value in CODE.items():
            if char == value:
                sentence += key
    return sentence.lower()

code = '.... . .-.. .-.. --- _ .-- --- .-. .-.. -.. '
print(convert_to_text(code))

text = 'I love python'
print(convert_to_morse(text))
    
    