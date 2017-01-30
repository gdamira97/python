a = input()
n = a.split()
for i in range(len(n)):
    n[i] = int(n[i])
    for j in range(i, len(n)):
        if n[i] > n[j]:
            n[i],n[j] = n[j],n[i]
for i in range(len(n)):
    print(i, end = '')
