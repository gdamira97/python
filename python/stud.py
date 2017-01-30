class students(object):
    def __init__(self):
        self.stud={}
    def add_student(self, name, gpa=0.0):
        if name not in self.stud:
            self.stud[name] = gpa
        for k, v in self.stud.items():
            print (k, '-', v)
    def top_3(self):
        if len(self.stud)==3:
            for k, v in sorted(([v, k] for [k, v] in self.stud.items()), reverse = True):
                print (v, '-', k)
        else:
            self.stud = sorted(([v, k] for [k, v] in self.stud.items()), reverse = True)
            for i in range(3):
                print(i+1,'. ', self.stud[i])
