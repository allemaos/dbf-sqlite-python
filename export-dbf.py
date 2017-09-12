#!/usr/bin/env python

import sys
print(sys.version)

# import the library
import urllib

from dbfread import DBF
table = DBF('files/final.dbf')
# writer.writerow(table.field_names)


for record in table:
    # writer.writerow(list(record.values()))
    print(record)

