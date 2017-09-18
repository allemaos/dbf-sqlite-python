#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from tabulate import tabulate
import dbf  


con = lite.connect('db/sqlite3.db')

with con:    
    
    cur = con.cursor()    

    cur.execute('PRAGMA table_info( case01_output_table)')
        
    data = cur.fetchall()
    
    for d in data:
        # print d[0],  d[1], d[2]
        print "%s:  %s \t%s" % (d[0] , d[1] , d[2])


    print "\nPrint Table \"temptable\" data with columns names: "
    # cur.execute("SELECT * FROM final where id < 20")
    cur.execute("SELECT * FROM case01_output_table")
    col_names = [cn[0] for cn in cur.description]
    
    rows = cur.fetchall()
    
    # print tabulate(rows, col_names, tablefmt="grid")
    print tabulate(rows, col_names)


