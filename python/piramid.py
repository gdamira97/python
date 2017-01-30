import random
n=int(input("n:"))
'''for x in range(0,n+1):
    print ("_"*(n-x), '%s%d%s'%(str(random.randint(1,9))*x, random.randint(1,9), str(random.randint(1,9))*x), (n-x)*"_")
'''
'''print(' '*n, 'M', ' '*n, '\n',
        ' '*(n-i), '/', '\\', ' '*(n-i), '\n',
        ' '*(n-i), random.randint(1,9), ' ', random.randint(1,9), ' '*(n-2), '\n',
        ' '*(n-3), '/', '\\', '/', '\\', ' '*(n-3), '\n',
        ' '*(n-4), random.randint(1,9), ' ', random.randint(1,9), ' ', random.randint(1,9), ' '*(n-4))
'''
'''print(' '*n, 'M', ' '*n, '\n', ' '*(n-i*2), '/', '\\', ' '*(n-i*2), '\n', ' '*(n-i*3), random.randint(1,9), ' ', random.randint(1,9), ' '*(n-i*3))'''
i=1
while i<2:
    i+=1
    print('%s M %s \n %s / \\%s \n %s %d %s %d %s'%(' '*(n-i), ' '*(n-i), ' '*(n-i*2), ' '*(n-i*2), ' '*(n-i*4), random.randint(1,9), ' ', random.randint(1,9), ' '*(n-i*4)))

