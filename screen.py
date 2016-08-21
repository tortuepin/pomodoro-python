import curses
import timeUtil
class CursesTimer:
    '''
    cursesを使ったタイマーを扱うクラス
    '''
    

    def __init__(self):
        self.sec = 3

    def setSecond(self, second):
        '''
        秒数を受け取り、self.secにセットする。
        引数    :self
                :second 秒数
        タイマーは受け取った秒数動作する
        '''
        self.sec = second 

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

    def curses_main(self):
        '''
        タイマー本体
        cursesを起動して、setSecondで指定された秒数数える
        '''
        t = timeUtil.Timer() #タイマーの初期化
        w = curses.initscr() #cursesの初期化
        curses.noecho()
        curses.cbreak()
        now = 0
        w.timeout(0)
        #セットされた時間になるまで0.1秒ごとに経過時間を表示する
        while now <= self.sec:
            now = t.getModifiedTime()
            w.addstr(str(now)+"\n press 's' key: stop\n press 'p' key: pause")
            w.refresh()
            timeUtil.time.sleep(0.1)
            w.clear()
            ch = self.interrupt(w)
            if ch is not True:
                if ch == ord('s'):
                    break
                elif ch == ord('p'):
                    t.pause()
                    w.timeout(-1)
                    w.addstr(str(now) + 
                            "\n press 's' key: stop\n press else key: restart")
                    ch = w.getch()
                    if ch == ord('s'):
                        break
                    w.timeout(0)
                    t.restart()

        curses.nocbreak()
        w.keypad(0)
        curses.echo()
        curses.endwin()


def main(self):
    c = CursesTimer()
    c.setSecond(10)
    c.curses_main()


curses.wrapper(main)

