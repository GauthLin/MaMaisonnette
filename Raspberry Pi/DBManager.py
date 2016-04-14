#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector


class DBManager:
    def __init__(self):
        self.connection = mysql.connector.connect(user='root',
                                                  password='domo',
                                                  host='127.0.0.1',
                                                  database='db_domo')

    def executeUpdate(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        cursor.close()

    def executeQuery(self, sql):
        pass
