class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def printTime(self):
        print(self.hour, ":", self.minute, ":", self.second)
    def after(self, other):
        if self.hour > other.hour or self.minute > other.minute or self.second > other.second:
            return True
        else:
            return False
