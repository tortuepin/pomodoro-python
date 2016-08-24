import CursesTimer
import Audio
import Utils
import database

class Pomodoro:
    '''
    pomodoro関連
    '''

    def __init__(self):
        self.db = database.database()
        self.NofPomodoro = 4 #休憩まで何回ポモドーロするか
        self.workTime = 25 #1ポモドーロ何分か
        self.sBreakTime = 5 #短い休みは何分
        self.lBreakTime = 15 #長い休みは何分
        self.t = CursesTimer.CursesTimer()
        self.minute = 60
        self.workComment = "Working"
        self.shortBreakComment = "Break"
        self.longBreakComment = "LongBreak"
        self.audio = Audio.Audio()
        self.audio.setAudio_file("bell.mp3")
        self.pomodoroCount = self.db.getTodaysPomodoro()

        self.u = Utils.Utils()
        



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
        self.t.setStrings(self.u.count_str(self.pomodoroCount))
        return self.t.start_Timer(self.workTime*self.minute)

    def start_s_Break(self):
        '''
        おやすみタイマー起動
        '''
        self.t.initStrings()
        self.t.setStrings(self.shortBreakComment)
        self.t.setStrings(self.u.count_str(self.pomodoroCount))
        return self.t.start_Timer(self.sBreakTime*self.minute)
    
    def start_l_Break(self):
        '''
        長いおやすみタイマー起動
        '''
        self.t.initStrings()
        self.t.setStrings(self.longBreakComment)
        self.t.setStrings(self.u.count_str(self.pomodoroCount))
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
                self.pomodoroCount += 1
                self.db.insertPomodoro()
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
