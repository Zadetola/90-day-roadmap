with open('sample.txt', 'r') as file:
    text = file.read()
char_count = len(text)
print('Characters:', char_count)
lines = text.split('\n')
line_count = len(lines)
print('lines:', line_count)
words = text.split()
word_count = len(words)
print('words:', word_count)
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
       
best_word = ''
best_count = 0
for word in counts:
    if counts[word] > best_count:
        best_word = word
        best_count = counts[word]
print('Most common:',best_word,best_count)