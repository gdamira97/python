printSymbol():
a=input('input any symbol')
if ord(a)>=65 and ord(a)<97:
    print('This symbol is capital letter')
elif ord(a)>=97 and ord(a)<123:
    print('This symbol is small letter')
elif ord(a)>=48 and ord(a)<58:
    print('This symbol is digit')
