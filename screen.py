import curses
import timeUtil

def curses_main(self):
    t = timeUtil.Timer() #タイマーの初期化
    w = curses.initscr() #cursesの初期化
    for i in range(0, 10):
        w.addstr(str(t.getTime()))
        w.refresh()
        timeUtil.time.sleep(1)
        w.clear()
        
    
    

curses.wrapper(curses_main)

