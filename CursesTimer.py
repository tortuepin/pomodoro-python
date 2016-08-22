import curses
import timeUtil
class CursesTimer:
    '''
    cursesを使ったタイマーを扱うクラス
    '''
    

    def __init__(self):
        self.sec = 0
        self.func = 0
        #funcが0ならストップウォッチ1ならタイマー


    def setSecond(self, second):
        '''
        秒数を受け取り、self.secにセットする。
        引数    :self
                :second 秒数
        タイマーは受け取った秒数動作する
        '''
        self.sec = second 

    def setTimer(self, second):
        '''
        秒数を受け取りfuncを1に
        引数    :self
                :second 秒数
        '''

        self.setSecond(second)
        self.func = 1

    def setStopwatch(self):
        '''
        funcを0にしてsecondに-1を
        '''
        self.func = 0
        self.sec = -1


    def interrupt(self, w):
        '''
        文字列の入力を検知
        
        引数    :self
                :cursesのインスタンス

        何か入力があった場合は入力された文字列を返す

        '''
        ch = w.getch()
        if ch is not -1:
            return ch
        else:
            return True

    def display_time(self, w, now, string):
        '''
        時間を表示する

        引数    :self
                :cursesのインスタンス
                :秒数

        '''
        if self.func == 0:
            w.addstr(str(now) + string)
        elif self.func == 1 and now < self.sec:
            w.addstr(str(round((self.sec - now), 1)) + string)
        w.refresh()

    def curses_main(self):
        '''
        タイマー本体
        cursesを起動して、setSecondで指定された秒数数える
        もし途中で中断したらFalseを返す
        '''
        bFlag = False
        t = timeUtil.Timer() #タイマーの初期化
        w = curses.initscr() #cursesの初期化
        curses.noecho()
        curses.cbreak()
        now = 0
        w.timeout(0)

        #セットされた時間になるまで0.1秒ごとに経過時間を表示する
        while now < self.sec or self.sec == -1:
            now = t.getModifiedTime()
            #w.addstr(str(now)+"\n press 's' key: stop\n press 'p' key: pause")
            #w.refresh()
            self.display_time(w,now, "\n press 's' key: stop\n press 'p' key: pause")
            timeUtil.time.sleep(0.1)
            w.clear()
            ch = self.interrupt(w)
            if ch is not True:
                if ch == ord('s'):
                    bFlag = True
                    break
                elif ch == ord('p'):
                    t.pause()
                    w.timeout(-1)
                    #w.addstr(str(now) + 
                    #        "\n press 's' key: stop\n press else key: restart")
                    self.display_time(w, now, "\n press 's' key: stop\n press else key: restart")
                    ch = w.getch()
                    if ch == ord('s'):
                        bFlag = True
                        break
                    w.timeout(0)
                    t.restart()

        curses.nocbreak()
        w.keypad(0)
        curses.echo()
        curses.endwin()
        return bFlag == False


    def start_Timer(self, sec):
        self.setTimer(sec)
        #curses_mainを起動
        return self.curses_main()

    def start_Stopwatch(self):
        self.setStopwatch()
        return self.curses_main()


