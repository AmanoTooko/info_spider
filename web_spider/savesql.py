import pymysql

class SqlManager:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='LNTU',passwd='123456',db='lntu',port=3306,charset='utf8')
        self.cur=self.conn.cursor()
    def select(self):
        pass
    def base_insert(self,data):
        self.cur.execute("INSERT INTO `student_info` (`number`, `name`, `sex`, `year`, `academy`, `majority`, `class`, `photo`) VALUES (%s,%s, %s, NULL, NULL, NULL, NULL, \'/1\')",data )
        self.conn.commit()




#data = cur.fetchall()

#cur.close()
#conn.close()


#print (data)