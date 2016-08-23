import time
import sys
import shutil

class Utils:

    def __init__(self):
        pass

    def progress_bar(self, progress):
        '''
        プログレスバーの文字列を返す
        '''
        max_len = int(self.get_terminal_columns()/3 * 2)
        bar_len = int(max_len*progress)
        return ('[' + '=' * bar_len +
                ('>' if bar_len < max_len else '') +
                ' ' * (max_len - bar_len) +
                ']')# %.1f%%' % (progress * 100.))

    def get_terminal_columns(self):
        '''
        ターミナルの列数を返す
        '''
        return shutil.get_terminal_size().columns

    def get_terminal_lines(self):
        '''
        ターミナルの行数を返す
        '''
        return shutil.get_terminal_size().lines

    def get_columns_space(self):
        '''
        ターミナルの列数分の空白を返す
        表示を調節する時に使おう
        '''
        return " " * int(self.get_terminal_columns())
    
    def count_bar(self, count):
        '''
        回数分の棒を返す
        '''
        s = " "
        for i in range(0,count):
            s += "|"
            if (i+1) % 5 == 0:
                s += "  "
        return s
    def count_str(self, count):
        '''
        回数表示のためのstrを返す
        '''
        s = "\n PomodoroCount = " + str(count) + "\n " + self.count_bar(count)
        return s


#u = Utils()
