import subprocess
import shutil
import threading
import time

class Audio:
    '''
    Audio関連
    '''

    def __init__(self):
        self.audio_file = ""

    def setAudio_file(self, audio_file):
        '''
        再生するファイルを指定する
        '''
        self.audio_file = audio_file

    def play(self):
        '''
        ファイルを再生する
        事前にsetAudio_file()で再生するファイルを指定しておくこと
        '''

        if shutil.which('afplay'):
            subprocess.call(["afplay", self.audio_file])




    def subthread_play(self):
        th = threading.Thread(target=self.play)
        th.start()

