class dbQuery:

    def __init__(self):
        self.C_pomodoro = "CREATE TABLE pomodoro (year integer, month integer, day integer, hour integer, minute integer, workID integer);"

        self.queryDic = {"create_pomodoro":self.C_pomodoro}



    def getQuery(self, name):
        if name in self.queryDic:
            return self.queryDic[name]
        else:
            return None

