# -*- coding: utf-8 -*-
import curses

def curses_main(args):
    w    = curses.initscr()
    curses.echo()
    while 1:
        w.addstr(0, 0, ">")
        w.clrtoeol()
        s   = w.getstr()
        if s == "q":    break
        w.insertln()
        w.addstr(1, 0, "[" + s + "]")

curses.wrapper(curses_main)
