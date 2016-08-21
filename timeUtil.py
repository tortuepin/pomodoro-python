import time

class Timer:
    def __init__(self):
        self.startTime = time.time()
        self.pauseTime = 0
        self.invalidTime = 0

    def setTime(self, t):
        self.startTime = t

    def getTime(self):
        return time.time() - self.startTime - self.invalidTime

    def getNow(self):
        return time.time()

    def getModifiedTime(self):
        return round(self.getTime(), 3)

    def pause(self):
        self.pauseTime = time.time()

    def restart(self):
        self.invalidTime += time.time() - self.pauseTime
        
