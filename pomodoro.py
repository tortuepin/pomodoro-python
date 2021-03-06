import CursesTimer
import Audio
import Utils
import database
import datetime

class Pomodoro:
    '''
    pomodoro関連
    '''

    def __init__(self):
        self.db = database.database() 
        self.t = CursesTimer.CursesTimer()
        self.u = Utils.Utils()

        self.NofPomodoro = 4    #休憩まで何回ポモドーロするか
        self.workTime = 25      #1ポモドーロ何分か
        self.sBreakTime = 5     #短い休みは何分
        self.lBreakTime = 15    #長い休みは何分
        self.minute = 60        #1分間は

        self.workComment = "Working"
        self.shortBreakComment = "Break"
        self.longBreakComment = "LongBreak"

        self.audio = Audio.Audio()
        self.audio.setAudio_file("bell.mp3")

        self.pomodoroCount = self.db.getTodaysPomodoro() #今日何回ポモドーロしたか

        self.dayend = 0                     #1日の終わりを何時にするか(0~23)
        today = datetime.datetime.today()   #今日の日付

        #次の１日の終わり
        self.nextEndDatetime = datetime.datetime.today().\
                replace(hour = self.dayend, minute = 0, second = 0, microsecond = 0)
        #もし今のhourがdayendより前ならenddatetimeは今日
        if today.hour < self.dayend:
            self.nextEndDatetime = self.nextEndDatetime.replace(day = today.day)
        #もし今のhourがdayendより後ならenddatatimeは明日
        if today.hour >= self.dayend:
            self.nextEndDatetime = self.nextEndDatetime.replace(day = today.today().day + 1)
        


        




    def endOfDay(self):
        '''
        1日が終わった時に呼び出される関数

        countをリセットし、次の1日が終わる時間を作る
        '''
        self.initPomodoroCount();
        today = datetime.datetime.today()
        #もし今のhourがdayendより前ならenddatetimeは今日
        if today.hour < self.dayend:
            self.nextEndDatetime = self.nextEndDatetime.replace(day = today.day)
        #もし今のhourがdayendより後ならenddatatimeは明日
        if today.hour >= self.dayend:
            self.nextEndDatetime = self.nextEndDatetime.replace(day = today.today().day + 1)

    def initPomodoroCount(self):
        self.pomodoroCount = 0

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
                #もし1日が終わったら
                if datetime.datetime.today() > self.nextEndDatetime:
                    self.endOfDay()

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


    def show_pomodoro(self):
        '''
        pomodoroした回数を表示する
        '''
        
        #今週の配列を初期化
        thisWeek = [0 for i in range(7)]
        #先週の配列を初期化
        lastWeek = [0 for i in range(7)]
        #今日の曜日を取得
        day = datetime.date.today()
        dayofweek = day.weekday()
        #今週分の回数を取得
        while dayofweek >= 0:
            thisWeek[dayofweek] = self.db.getdaysPomodoro(day.year, day.month, day.day)
            dayofweek -= 1
            day = day - datetime.timedelta(days=1)
        for i in range(6, -1, -1):
            lastWeek[i] = self.db.getdaysPomodoro(day.year, day.month, day.day)
            day = day - datetime.timedelta(days=1)
        print("今週")
        print("月 火 水 木 金 土 日")
        for i in thisWeek:
            print('{0:02d}'.format(i), end=" ")
        print()
        print("先週")
        print("月 火 水 木 金 土 日")
        for i in lastWeek:
            print('{0:02d}'.format(i), end=" ")
        print()



        
        
