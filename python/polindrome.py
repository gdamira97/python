a = open('text.txt', 'r')
line = a.readline()
p = {}
for word in line.split():
    word = word.lower()
    for char in word:
        if char in '.,?!':
            word = word.strip(char)
    for i in range(len(word)):
        for j in range(len(word)+1):
            b = word[i:j]
            c = word[::-1]
            if b == c:
                if len(word) <= len(b):
                    word = b
                    p[word] = p.get(word, 0) + 1
for key, value in sorted(([value, key] for [key, value] in p.items()), reverse = True):
    print ('%s - %s'%(value, key))
