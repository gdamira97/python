import string
def months(s):
    if s == "January":
        return '01'
    if s == "February":
        return '02'
    if s == "March":
        return '03'
    if s == "April":
        return '04'
    if s == "May":
        return '05'
    if s == "June":
        return '06'
    if s == "July":
        return '07'
    if s == "August":
        return '08'
    if s == "September":
        return '09'
    if s == "October":
        return '10'
    if s == "November":
        return '11'  
    if s == "December":
        return '12'
file1 = open("remind.txt","r")
t=[]
a = file1.readline()
while a!="the end":
    b = a.split()
    t.append(b)
    a = file1.readline()
z=[]

for i in t:
    s=""
    for j in i:
        if j=="on":
            break
        s=s+j+" "
    z.append(s)
y=[]
for i in t:
    if "of" in i:
        m=months(i[-1])
        d = i[-3][:-2]
    else:
        m=i[-1][-2:]
        d=i[-1][:2]
    y.append([d,m])
swapped=True
while(swapped):
    swapped=False
    for i in range(len(y)-1):
        if(int(y[i][1])>int(y[i+1][1])):
                swapped = True
                y[i],y[i+1]=y[i+1],y[i]
                z[i],z[i+1]=z[i+1],z[i]
        if(int(y[i][1])==int(y[i+1][1])):
            if(int(y[i][0])>int(y[i+1][0])):
                swapped = True
                y[i],y[i+1]=y[i+1],y[i]
                z[i],z[i+1]=z[i+1],z[i]    
for i in range(len(z)):
    if len(y[i][0])==1:
        print ("0"+y[i][0]+"."+y[i][1]+": "+z[i])
    else: print (y[i][0]+"."+y[i][1]+": "+z[i])

