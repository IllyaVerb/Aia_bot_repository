import psycopg2
from settings import host, database, user, password
import time
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import os
# conn = psycopg2.connect(host=host,
#                         database=, user=user,
#                         password=password)

class DB_connector():

    def __init__(self, host,database, user, password):
        self.conn = psycopg2.connect(host=host,
                                database=database, user=user,
                                password=password)
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.conn.cursor()
        print('db connected')

    def add_user(self, id, first_name=None, last_name=None, username=None):
        try:
            sql = "INSERT INTO users(user_id, first_name, last_name, username)\
                         VALUES(%s, %s, %s, %s);"

            self.cursor.execute(sql, (id, first_name, last_name, username))
            # self.conn.commit()

            # get the part id
            # last = self.cursor.fetchone()
            return
        except (Exception, psycopg2.DatabaseError) as error:
            print('error:')
            print(error)

    def add_logs(self, action, datetime, user_id, reply_text):
        try:
            sql = "INSERT INTO logs(action, datetime, user_id, reply_text)\
                         VALUES(%s, %s, %s, %s);"

            self.cursor.execute(sql, (action, datetime, user_id, reply_text))
            print('executed')
            # self.conn.commit()
            return
        except (Exception, psycopg2.DatabaseError) as error:
            print('error:')
            print(error)

    def show_all_users(self):
        try:
            sql = """SELECT user_id, first_name, last_name, username FROM users"""
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            s = ''
            n = 1
            while row is not None:
                # print(row)
                s += '{n} {id} {name} @{username}'.format(n=n, id=row[0], name=row[1], username=row[-1]) + '\n'
                row = self.cursor.fetchone()
                n+=1
            return s
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_user_by_id(self, id):
        try:

            sql = """SELECT user_id, first_name, last_name, username FROM users WHERE user_id={id}""".format(id=id)
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            # print(row)
            # self.conn.commit()
            return row
        except (Exception, psycopg2.DatabaseError) as error:
            print('error:')
            print(error)

    def get_users_number(self):
        try:
            sql = """SELECT COUNT(*) FROM users"""
            self.cursor.execute(sql)
            row = self.cursor.fetchone()[0]
            return row
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_logs_len(self):
        try:
            sql = """SELECT COUNT(*) FROM logs"""
            self.cursor.execute(sql)
            row = self.cursor.fetchone()[0]
            return row
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_logs(self):
        try:
            sql = """SELECT user_id FROM logs"""
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_all_user_id(self):
        try:
            sql = 'select user_id from users'
            self.cursor.execute(sql)
            id_list = self.cursor.fetchall()
            return id_list
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_advice_by_text(self, text):
        """Find advice in advices table and return id of advice or None"""
        try:
            sql = "SELECT id, advice, is_daily_adv FROM advices where advice = '{}'".format(text)
            self.cursor.execute(sql)
            adv = self.cursor.fetchone()
            # print(adv)
            if adv != None:
                return adv[0]
            else:
                return None
        except (Exception, psycopg2.DatabaseError) as error:
            print('error:')
            print(error)

    def get_advice_by_id(self, id):
        """Find advice in advices table and return id of advice or None"""
        try:
            sql = "SELECT id, advice, is_daily_adv FROM advices where id = '{}'".format(id)
            self.cursor.execute(sql)
            adv = self.cursor.fetchone()
            # print(adv)
            if adv != None:
                return adv[1]
            else:
                return None
        except (Exception, psycopg2.DatabaseError) as error:
            print('error:')
            print(error)

    def add_advice(self, advice, is_daily_advice=0):
        try:
            sql = "INSERT INTO advices(advice, is_daily_adv)\
                                     VALUES(%s, %s);"
            self.cursor.execute(sql, (advice, is_daily_advice))
            adv_id = self.get_advice_by_text(advice)
            return adv_id

        except (Exception, psycopg2.DatabaseError) as error:
            print('error:')
            print(error)

    def get_users_adv_list(self, user_id):
        try:
            sql = """select advice from advices 
                right join users_advices on advices.id = users_advices.advice_id 
                where users_advices.user_id = {}""".format(user_id)
            self.cursor.execute(sql)
            adv_list = self.cursor.fetchall()
            return adv_list

        except (Exception, psycopg2.DatabaseError) as error:
            print('error:')
            print(error)

    def drop_saved_advice(self, advice):
        try:
            adv_id = self.get_advice_by_text(advice)
            if adv_id != None:
                sql = "DELETE FROM users_advices WHERE advice_id = '{}'".format(adv_id)
                self.cursor.execute(sql)
            return

        except (Exception, psycopg2.DatabaseError) as error:
            print('error:')
            print(error)

    def add_users_advice(self, user_id, advice_id):
        try:
            sql = "INSERT INTO users_advices(user_id, advice_id)\
                                     VALUES(%s, %s);"
            self.cursor.execute(sql, (user_id, advice_id))
            return

        except (Exception, psycopg2.DatabaseError) as error:
            print('error:')
            print(error)


if __name__ == '__main__':
    connector = DB_connector(host, database, user, password)
    connector.add_advice('Делай что любишь блять!', 0)
    # while 1:
    #     id = input()
    #
    #     if connector.get_user_by_id(id)==None:
    #         connector.add_user(id,'Vlad','Bandurin', 'vladkrutoi')
    #
    #     else:
    #         print('error')
    #     connector.show_all_users()
    # datetime = time.ctime()
    # connector.add_logs(r'\action', datetime, 1234, '???')
    print(connector.get_all_user_id())
    # t = time.time()
    # connector.add_logs(123,123, t)
    # print(connector.get_user_by_id(12234)==None)
    print('done')