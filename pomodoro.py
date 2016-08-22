import CursesTimer

class Pomodoro:
    '''
    pomodoro関連
    '''

    def __init__(self):
        self.NofPomodoro = 4
        self.workTime = 25
        self.sRestTime = 5
        self.lRestTime = 15
        self.t = CursesTimer.CursesTimer()
        self.minute = 1
        self.workComment = " Work!! Work!! Work!!\n"
        self.restComment = " Break\n"



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

    def setsRestTime(self, m):
        '''
        短い休みを何分にするかを設定
        '''
        self.sRestTime = m

    def setlRestTime(self, m):
        '''
        長い休みを何分にするかを設定
        '''
        self.lRestTime = m


    def start_work(self):
        '''
        仕事タイマー起動
        '''
        self.t.initStrings()
        self.t.setStrings(self.workComment)
        return self.t.start_Timer(self.workTime*self.minute)

    def start_s_rest(self):
        '''
        おやすみタイマー起動
        '''
        self.t.initStrings()
        self.t.setStrings(self.restComment)
        return self.t.start_Timer(self.sRestTime*self.minute)
    
    def start_l_rest(self):
        '''
        長いおやすみタイマー起動
        '''
        return self.t.start_Timer(self.lRestTime*self.minute)
        

    def pomodoro(self):
        '''
        pomodoro本体
        '''
        n = 0
        bFlag = False
        while 1: 
            while n < self.NofPomodoro:
                if self.start_work() == False:
                    bFlag = True
                    break
                if self.start_s_rest() == False:
                    bFlag = True
                    break
            if bFlag == True:
                break
            self.start_l_rest()


p = Pomodoro()
p.pomodoro()
