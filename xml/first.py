# -*- coding: utf8 -*-

import xml.etree.ElementTree as etree

root = etree.Element('orders')
order = etree.Element('order')
order.text = 'some thing...'
root.append(order)
print(etree.tostring(root))
