def normaLize_date(date):
    w=date.split(".")
    if(len(w) != 2 or w[0].isdigit() == False or w[1].isdigit() == False):
        w=date.split()
        new_date=""
        for k in w[0]:
            if(k.isdigit()):
                new_date=new_date+k
        if(len(new_date)==1):
            new_date="0"+new_date
        new_month=m[w[-1].lower()]
        date=new_date+"."+new_month
    return date

a=open('freeday.txt','r')
lines=a.read().split('\n')
m={'january':'01','february':'02','march':'03','april':'04','may':'05','june':'06','july':'07','august':'08','september':'09','october':'10','november':'11','december':'12'}

form={}
for line in lines:
    w=line.split(' on ')
    form[normaLize_date(w[1])]=w[0]

dates=list(form)

for i in range(len(dates)):
    for j in range(len(dates)+1):
        w1=dates[j].split('.')
        w2=dates[j+1].split('.')
        if (w1[1]>w2[1] or (w1[1]==w2[1] and w1[0]>w2[1])):
               temp=dates[j]
               dates[j]=dates[j+1]
               dates[j+1]=temp

for key in dates:
    print (key,"1",form[key])
