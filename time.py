import time

class Timer:
    def __init__(self):
        self.stime = 0


    def setTime(self):
        self.stime = time.time()

    def getTime(self):
        return time.time() - self.stime


