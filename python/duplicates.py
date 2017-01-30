a = open('hello.txt', 'r')
for line in a:
    for word in line.split():
        worddup = []
        worddup = worddup.append(word)
for i in range(0, len(worddup)):
        for x in range(i + 1, len(worddup)):
            if worddup[i] == worddup[x]:
                return True
    return False
for i in worddup:
    print(i, end = ' ')
