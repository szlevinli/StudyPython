# -*- coding: utf8 -*-

import mysql.connector

optionFiles = 'connnector_config.ini'
try:
    cnx = mysql.connector.connect(option_files=optionFiles)
except mysql.connector.Error as err:
    print(err)
else:
    cnx.close()
