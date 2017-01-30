a=open('hello.txt', 'r')
wordcs = {}
line=a.readline()
print(line)
for word in line.split():
    word = word.lower()
    for char in word:
        if char in ',?.!/;:':
            word = word.strip(char)
    wordcs[word] = wordcs.get(word, 0)+1
for k, v in sorted([(value,key) for (key,value) in wordcs.items()], reverse = True):
    print(v, '-',  k)
