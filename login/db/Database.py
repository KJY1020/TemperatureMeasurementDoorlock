import pymysql
import time

class Database:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='ubuntudb', password='1q2w3e4r', db='class02')
        self.cur = self.db.cursor()
        print("good")

    def selectAllJson(self):
        sql = "select * from recorddht;"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def selectAllLogin(self):
        sql = "select * from login;"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def insertJson(self, hum, temper):
        tm = time.localtime()
        yeardate = "{}-{}-{}".format(tm.tm_year, tm.tm_mon, tm.tm_mday)
        nowtime = "{}:{}:{}".format(tm.tm_hour, tm.tm_min, tm.tm_sec)
        sql = "insert into recorddht(data) values(%s);"
        val = ('{{"yeardate":"{}", "time":"{}", "hum":"{}", "temper":"{}"}}'.format(yeardate, nowtime, hum, temper))
        self.cur.execute(sql, val)
        self.db.commit()
        return "good"

    def insertLogin(self, userID, userPW):
        sql = "insert into login(userID, userPW) values(%s,%s);"
        self.cur.execute(sql, (userID, userPW))
        self.db.commit()
        return "good"
