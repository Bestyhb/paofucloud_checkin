import pymysql


class MySQL():

    __init__(self):
    def db(self,check_data):
        sql = "INSERT INTO SIGN.paofu_checkin (now(),{})".format(check_data)
        #执行SQL语句

if __name__=="__main__":
    test=MySQL()
    test.db(543)
    sql = "SELECT DATA FROM SIGN.paofu_checkin WHERE DATE LIKE '%hour(now())%' "
    commit(sql)