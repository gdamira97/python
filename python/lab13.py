class Stack(object):
        def __init__(self):
            self.smth=[]
        def push(self, smth):
            self.smth.append(smth)
        def pop(self):
            self.smth.pop()
        def peak(self):
            for i in range(len(self.smth)):
                print (self.smth[i], end = ' ')
