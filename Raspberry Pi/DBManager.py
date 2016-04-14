#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql.cursors


class DBManager:
    def __init__(self):
        self.connection = pymysql.connect(user='client',
                                          passwd='domo',
                                          host='localhost',
                                          database='db_domo')

    def executeUpdate(self, sql, para):
        print(sql)
        cursor = self.connection.cursor()
        cursor.execute(sql, para)
        self.connection.commit()
        cursor.close()
        self.connection.close()
    def executeQuery(self, sql):
        pass
