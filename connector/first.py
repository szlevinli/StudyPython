# -*- coding: utf8 -*-

import mysql.connector

optionFiles = 'connnector_config.ini'
query = (" select"
         "    t.cust_code"
         "    ,t.start_dt"
         " from"
         "    tmp_03 t"
         " limit %s, %s")
try:
    cnx = mysql.connector.connect(option_files=optionFiles)
    cursor = cnx.cursor()
    cursor.execute(query, (0, 10))

    for cust_code, start_dt in cursor:
        print("cust_code=", cust_code, sep='{', end='} ')
        print("start_dt=", start_dt, sep='{', end='}\n')

except mysql.connector.Error as err:
    print(err)
else:
    cursor.close()
    cnx.close()
