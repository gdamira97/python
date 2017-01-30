a = open('hello.txt', 'r')
worddup = {}
for line in a:
    print (line)
    for word in line.split():
        word = word.lower()
        for char in word:
            if char in ',?.!/;:':
                word = word.strip(char)
        worddup[word] = worddup.get(word, 0)
for k in sorted(worddup.keys()):
    print(k, end = ' ')
