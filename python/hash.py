import hashlib

def hash():
    '''a=input('Enter text')
    b=md5.new()
    b.update(a)
    print(b)'''
    
    print (hashlib.md5("whatever your string is").hexdigest())
hash()
