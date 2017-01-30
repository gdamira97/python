a=int(input('Input mark'))
if a>=95:
    print('A')
elif a>=90 and a<95:
    print('-A')
elif a>=85 and a<90:
    print('+B')
elif a>=80 and a<85:
    print('-B')
elif a>=75 and a<80:
    print('-B')
elif a>=70 and a<75:
    print('+C')
elif a>=65 and a<70:
    print('C')
elif a>=60 and a<65:
    print('-C')
elif a>=55 and a<60:
    print ('+D')
elif a>=50 and a<55:
    print('D')
elif a<50:
    print('F')
