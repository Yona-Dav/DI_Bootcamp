
text = input('Enter a text')

de_code = input("Do you want to encrypt or to decrypt")
shift = int(input('Enter a number'))

new_encrypt = []
new_decrypt = []

# For specific shift of 3
# if de_code == 'encrypt':
#     s_text = text.split(' ')
#     for word in s_text:
#         for w in word:
#             if 96<ord(w)<123 or 64<ord(w)<91:
#                 if w=='x':
#                     new_encrypt+= 'a'
#                 elif w=='y':
#                     new_encrypt+='b'
#                 elif w=='z':
#                     new_encrypt += 'c'
#                 else:
#                     new_encrypt += chr(ord(w) + 3)
#         new_encrypt += ' '
#     new_encrypt = ''.join(new_encrypt)
#     print(new_encrypt)
# elif de_code == 'decrypt':
#     s_text = text.split(' ')
#     for word in s_text:
#         for w in word:
#             if 96<ord(w)<123 or 64<ord(w)<91:
#                 if w=='a':
#                     new_decrypt+= 'x'
#                 elif w=='b':
#                     new_decrypt+='y'
#                 elif w=='c':
#                     new_decrypt += 'z'
#                 else:
#                     new_decrypt += chr(ord(w) - 3)
#         new_decrypt += ' '
#     new_decrypt = ''.join(new_decrypt)
#     print(new_decrypt)


if de_code == 'encrypt':
    s_text = text.split(' ')
    for word in s_text:
        for w in word:
            if 96<ord(w)<123 or 64<ord(w)<91:
                new_letter = chr(ord(w) + shift)
                if 96<ord(new_letter)<123 or 64<ord(new_letter)<91:
                    new_encrypt += new_letter
                else:
                    if 90<ord(new_letter)<97:
                        new_letter = chr(ord(new_letter)-96+64)
                        new_encrypt += new_letter
                    elif ord(new_letter)>122:
                        new_letter = chr(ord(new_letter)-122+96)
                        new_encrypt += new_letter
            else:
                new_letter = w
                new_encrypt += new_letter
        new_encrypt += ' '
    new_encrypt = ''.join(new_encrypt)
    print(new_encrypt)
elif de_code == 'decrypt':
    s_text = text.split(' ')
    for word in s_text:
        for w in word:
            if 96<ord(w)<123 or 64<ord(w)<91:
                new_letter = chr(ord(w) - shift)
                if 96<ord(new_letter)<123 or 64<ord(new_letter)<91:
                    new_decrypt += new_letter
                else:
                    if 65>ord(new_letter):
                        new_letter = chr(90-64+ord(new_letter))
                        new_decrypt += new_letter
                    elif 91<ord(new_letter)<97:
                        new_letter = chr(122-96+ord(new_letter))
                        new_decrypt += new_letter
            else:
                new_letter = w
                new_decrypt += new_letter
        new_decrypt += ' '
    new_decrypt = ''.join(new_decrypt)
    print(new_decrypt)

