# -*- coding: utf8 -*-

from dbconnector import Connector, Cursor

if __name__ == '__main__':
    optionFiles = 'connnector_config.ini'
    query = (" select"
             "    t.order_id"
             "    ,t.order_no"
             " from"
             "    tt_express_order_rebate t"
             " limit %s, %s")
    d = {"dictionary": True}
    with Connector(optionFiles) as cnx:
        with Cursor(cnx, **d) as cur:
            print(repr(cur))
            cur.execute(query, (0, 10))
            rows = cur.fetchall()
            print(rows)
