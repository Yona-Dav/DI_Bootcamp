# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

sequence = input('Enter a comma separated sequence of words ')
print(sequence)

seq = sequence.split(',')
for i in range(len(seq)):
    if seq[i][0] != seq[i+1][0]:
        if ord(seq[i][0]) > ord(seq[i+1][0]):
            seq[i][0], seq[i+1][0] = seq[i+1][0], seq[i][0]

print(seq)

