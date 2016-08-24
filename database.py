import sqlite3
import datetime

class database:
    '''
    データベース関連
    '''
    
    def __init__(self):
        self.DBDirectory = "./dbs/"
        self.pomodoroDBName = "pomodoro.sqlite3" #ポモドーロした回数とか
        self.pomodoroTableName = "pomodoro"
        self.todoID = 0

    def insertPomodoro(self):
        '''
        データベースに１ポモドーロ登録する
        '''
        connector = sqlite3.connect(self.DBDirectory+self.pomodoroDBName)

        query = "insert into " + str(self.pomodoroTableName) + " values" +\
                datetime.datetime.today().strftime("(%Y,%m,%d,%H,%M,") +\
                str(self.todoID) + ")"
        connector.execute(query)

        connector.commit()
        connector.close()

    def getTodaysPomodoro(self):
        '''
        今日何回ポモドーロしたか返す
        '''
        connector = sqlite3.connect(self.DBDirectory+self.pomodoroDBName)

        query = "select count(*) from " + self.pomodoroTableName +\
                " where year = " + str(datetime.date.today().year) +\
                " and month = " + str(datetime.date.today().month) +\
                " and day = " + str(datetime.date.today().day)

        cursor = connector.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connector.close()

        return result[0][0]

        

