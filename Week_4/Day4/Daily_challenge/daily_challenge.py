import string

alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)

code = [['7','i','3'],
['T','s','i'],
['h','%','x'],
['i',' ','#'],
['s','M',' '],
['$','a',' '],
['#','t','%'],
['^','r','!']]

def decode_matrix(code):
    sentence=''
    for j in range(0,len(code[0])):
        for i in range(0,len(code)):
            for char in code[i][j]:
                if char in alphabet_lower or char in alphabet_upper:
                    sentence += char
                elif char==' ' or char=='#':
                    sentence +=" "
    return sentence



print(decode_matrix(code))
