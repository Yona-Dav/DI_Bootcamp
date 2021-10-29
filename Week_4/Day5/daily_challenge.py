# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

#sequence = input('Enter a comma separated sequence of words ')
sequence = 'without,hello,bag,world'
seq = sequence.split(',')
print(','.join(sorted(seq)))


# Use List Comprehension
result = ','.join(sorted((x for x in sequence.split(','))))
print(result)