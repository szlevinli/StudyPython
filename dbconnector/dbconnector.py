# -*- coding: utf8 -*-

import mysql.connector


class Connector:

    def __init__(self, optionfile):
        self.optionfile = optionfile

    def __enter__(self):
        self.cnx = mysql.connector.connect(option_files=self.optionfile)
        return self.cnx

    def __exit__(self, type, value, traceback):
        self.cnx.close()


class Cursor:

    def __init__(self, cnx, **kwargs):
        self.cnx = cnx
        self.kwargs = kwargs

    def __enter__(self):
        self.cursor = self.cnx.cursor(**self.kwargs)
        return self.cursor

    def __exit__(self, type, value, traceback):
        self.cursor.close()
