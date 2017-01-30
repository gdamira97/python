a=[]
b=0
for i in range(0,3):
    a.append([])
    for j in range(0,3):
        a[i].append(b)
        b+=1
for i in range(0,len(a)):
    print(a[i])
"""
    a=[1,2,3,4,5,6,7,8,9,0]
    for in range(0,len(a)-1):
        if i+1 == len(a):
            print(i)
            break
        for j in range[i+1, len(a)]:
            if a[i] == a[j]:
                a.pop(j)
                print(a)
"""
