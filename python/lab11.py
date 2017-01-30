a = input('Enter number of lines in attendance list: ')
n = int(a)
students = {} 
for i in range(n):
    stud, date, atten = list(map(str.strip, input().replace('-', ':').split(":")))
    stud = stud.split()[0]
    if stud not in students:
        students[stud] = {date: atten}
    else:
        students[stud].update({date: atten})
 
student = input('Enter student: ')
if student in students:
    for date, atten in students[student].items():
        print('%s - %s' % (date, atten))
