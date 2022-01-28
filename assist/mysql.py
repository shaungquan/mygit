import pymysql
from config import message
import sys


class Database:
    db = ''

    def __init__(self):
        try:
            self.db = pymysql.connect(host=message.host,
                                      user=message.user,
                                      password=message.password,
                                      database=message.database)
            self.cursor = self.db.cursor()
        except Exception as e:
            # 登录数据库失败则退出
            print("数据库登录失败！错误信息：", e)
            sys.exit()

    def create(self, sql):
        try:
            # 执行语句
            self.cursor.execute(sql)
            print("create语句执行成功！")
        except Exception as e:
            print("create失败！", e)

    def drop(self, sql):
        try:

            self.cursor.execute(sql)
            self.db.commit()
            print("drop语句执行成功！")
        except Exception as e:
            # 执行失败则数据库回滚
            self.db.rollback()
            print("drop失败！", e)

    def install(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("install语句执行成功！")
        except Exception as e:
            # 执行失败则数据库回滚
            self.db.rollback()
            print("install失败！", e)

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("update语句执行成功！")
        except Exception as e:
            # 执行失败则数据库回滚
            self.db.rollback()
            print("update失败！", e)

    def select(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print(data)

    def __del__(self):
        if type(self.db).__name__ == 'Connection':
            self.db.close()
        else:
            return


# a = Database()
# print(a)
# a.update("UPDATE `guo_1029`.`course` SET `CId` = '01', `Cname` = '大傻子', `TId` = '02' WHERE `CId` = '01' AND `Cname` = '语文' AND `TId` = '02' LIMIT 1;")
