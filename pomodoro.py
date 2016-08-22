import CursesTimer
import Audio

class Pomodoro:
    '''
    pomodoro関連
    '''

    def __init__(self):
        self.NofPomodoro = 1
        self.workTime = 5
        self.sBreakTime = 5
        self.lBreakTime = 15
        self.t = CursesTimer.CursesTimer()
        self.minute = 1
        self.workComment = "Working"
        self.shortBreakComment = "Break"
        self.longBreakComment = "LongBreak"
        self.audio = Audio.Audio()
        self.audio.setAudio_file("bell.mp3")
        



    def setNofPomodoro(self, num):
        '''
        ポモドーロ何回で長い休みにするかを設定
        '''
        self.NofPomodoro = num

    def setworkTime(self, m):
        '''
        １ポモドーロは何分にするかを設定
        '''
        self.workTime = m

    def setsBreakTime(self, m):
        '''
        短い休みを何分にするかを設定
        '''
        self.sBreakTime = m

    def setlBreakTime(self, m):
        '''
        長い休みを何分にするかを設定
        '''
        self.lBreakTime = m


    def start_work(self):
        '''
        仕事タイマー起動
        '''
        self.t.initStrings()
        self.t.setStrings(self.workComment)
        return self.t.start_Timer(self.workTime*self.minute)

    def start_s_Break(self):
        '''
        おやすみタイマー起動
        '''
        self.t.initStrings()
        self.t.setStrings(self.shortBreakComment)
        return self.t.start_Timer(self.sBreakTime*self.minute)
    
    def start_l_Break(self):
        '''
        長いおやすみタイマー起動
        '''
        self.t.initStrings()
        self.t.setStrings(self.longBreakComment)
        return self.t.start_Timer(self.lBreakTime*self.minute)
        

    def pomodoro(self):
        '''
        pomodoro本体
        '''
        bFlag = False
        while 1: 
            n = 0
            while n < self.NofPomodoro:
                if self.start_work() == False:
                    bFlag = True
                    break
                self.audio.subthread_play()
                if self.start_s_Break() == False:
                    bFlag = True
                    break
                self.audio.subthread_play()
                n += 1
            if bFlag == True:
                break
            if self.start_l_Break() == False:
                break
            self.audio.subthread_play()


p = Pomodoro()
p.pomodoro()
