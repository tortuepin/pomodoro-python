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
        max_len = self.get_terminal_columns() - 12
        bar_len = int(max_len*progress)
        return ('[' + '=' * bar_len +
                ('>' if bar_len < max_len else '') +
                ' ' * (max_len - bar_len) +
                '] %.1f%%' % (progress * 100.))

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

#u = Utils()
