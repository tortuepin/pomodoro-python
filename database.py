import sqlite3
import datetime
import dbQuery

class database:
    '''
    データベース関連
    '''
    
    def __init__(self):
        self.DBDirectory = "./dbs/"
        self.pomodoroDBName = "pomodoro.sqlite3" #ポモドーロした回数とか
        self.pomodoroTableName = "pomodoro"
        self.todoID = 0

        #もしテーブルがなかったら作る
        if not self.isTable(self.pomodoroTableName):
            name = "create_" + self.pomodoroTableName
            q = dbQuery.dbQuery()
            query = q.getQuery(name)
            if query is not None:
                self.exeQuery(query)




            

    def exeQuery(self, query):
        '''
        指定されたqueryを実行する
        '''

        connector = sqlite3.connect(self.DBDirectory+self.pomodoroDBName)

        connector.execute(self.query)

        connector.commit()
        connector.close()

            
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
        today = datetime.date.today()
        return self.getdaysPomodoro(today.year, today.month, today.day)
#        connector = sqlite3.connect(self.DBDirectory+self.pomodoroDBName)
#
#        query = "select count(*) from " + self.pomodoroTableName +\
#                " where year = " + str(datetime.date.today().year) +\
#                " and month = " + str(datetime.date.today().month) +\
#                " and day = " + str(datetime.date.today().day)
#
#        cursor = connector.cursor()
#        cursor.execute(query)
#        result = cursor.fetchall()
#        connector.close()
#
#        return result[0][0]

    def getdaysPomodoro(self, year, month, day):
        '''
        指定した日に何回ポモドーロしたか返す

        引数
        year
        month
        day
        '''
        connector = sqlite3.connect(self.DBDirectory+self.pomodoroDBName)

        query = "select count(*) from " + self.pomodoroTableName +\
                " where year = " + str(year) +\
                " and month = " + str(month) +\
                " and day = " + str(day)

        cursor = connector.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connector.close()

        return result[0][0]

    def isTable(self, tablename):
        '''
        テーブルの存在確認
        '''
        connector = sqlite3.connect(self.DBDirectory+self.pomodoroDBName)

        query = ("select * from sqlite_master where type = 'table' and name = '%s'")
        cur = connector.execute(query % tablename)

        if cur.fetchone() == None:
            print(tablename + "を作って")
            connector.close()
            return False
            
        connector.close()

        return True


        

        
db = database()
print(db.getdaysPomodoro(2016, 8, 25))
print(db.getTodaysPomodoro())
print(db.isTable("pomodoro"))
