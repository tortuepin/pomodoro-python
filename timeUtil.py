import time

class Timer:
    def __init__(self):
        self.stime = time.time()


    def setTime(self):
        self.stime = time.time()

    def getTime(self):
        return time.time() - self.stime


