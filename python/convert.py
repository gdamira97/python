system = input("Enter system of numbers: ")
number = input("Enter number: ")

def bin_dec(num):
    q = []
    q = num[::-1]
    s = 0
    for i in range(0, len(q)):
        a = int (q[i])*(2**i)
        s+=a
        
    return s
    
def oct_dec(num):
    q = []
    q = num[::-1]
    s = 0
    for i in range(0, len(q)):
        a = int (q[i])*(8**i)
        s+=a
        
    return s

def hex_dec(num):
    q = []
    q= num[::-1]
    s = 0
    for i in range(0, len(q)):
        if ord(q[i]) == 65:
            a = 10*(16**i)
        elif ord(q[i]) == 66:
            a = 11*(16**i)
        elif ord(q[i]) == 67:
            a = 12*(16**i)
        elif ord(q[i]) == 68:
            a = 13*(16**i)
        elif ord(q[i]) == 69:
            a = 14*(16**i)
        elif ord(q[i]) == 70:
            a = 15*(16**i)
        else:
            a=int (q[i])*(16**i)
        s+=a
        
    return s

def dec_bin(num):
    r=[]
    s=int(num)
    while s!=0:
        r.append(s%2)
        s //= 2
    r = r[::-1]
    
    return r

def dec_oct(num):
    r=[]
    s=int(num)
    while s!=0:
        r.append(s%8)
        s //= 8
    r = r[::-1]
    
    return r

def dec_hex(num):
    r=[]
    s=int(num)
    while s!=0:
        if s%16 == 10:
            r.append('A')
        elif s%16 == 11:
            r.append('B')
        elif s%16 == 12:
            r.append('C')
        elif s%16 == 13:
            r.append('D')
        elif s%16 == 14:
            r.append('E')
        elif s%16 == 15:
            r.append('F')
        else:
            r.append(s%16)
        s //= 16
    r = r[::-1]
    
    return r

if system == 'binary':
    print('binary:', number)
    x=bin_dec(number)
    y=dec_oct(x)
    print('octal:', end='')
    for i in y:
        print(i, end='')
    print()
    print('dec:', x)
    z=dec_hex(x)
    print('hexidecimal:', end='')
    for i in z:
        print(i, end='')
elif system == 'octal':
    x=oct_dec(number)
    y=dec_bin(x)
    print('bin:', end='')
    for i in y:
        print(i, end='')
    print()
    print('octal: ', number)
    print('dec', x)
    z=dec_hex(x)
    print('hexadecimal:', end='')
    for i in z:
        print(i, end='')
elif system == 'hexadecimal':
    x=hex_dec(number)
    y=dec_bin(x)
    print('bin:', end='')
    for i in y:
        print(i, end='')
    print()
    z=dec_oct(x)
    print('octal:', end='')
    for i in y:
        print(i, end='')
    print()
    print('decimal:', x)
    print('hexadecimal: ', number)
elif system == 'decimal':
    x=dec_bin(number)
    print('bin:', end='')
    for i in number:
        print(i, end='')
    print()
    y=dec_oct(number)
    print('octal:', end='')
    for i in number:
        print(i, end='')
    print()
    print('dec', number)
    number3=dec_oct(number)
    z=dec_hex(number)
    print('hexadecimal:', end='')
    for i in number:
        print(i, end='')
