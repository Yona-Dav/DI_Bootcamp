str = 'You have entered a wrong domain'

new_str = str.split(' ')

reverse_sentence = []
for i in range(len(new_str)-1,-1,-1):
    reverse_sentence.append(new_str[i])

reverse_str = ' '.join(reverse_sentence)

print(reverse_str)
