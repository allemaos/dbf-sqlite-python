#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from tabulate import tabulate
import dbf  


def print_table_info(table):
    cur.execute('PRAGMA table_info('+`table`+')')
    data = cur.fetchall()
    
    for d in data:
        # print d[0],  d[1], d[2]
        print "%s:  %s \t%s" % (d[0] , d[1] , d[2])

def print_table_from_query():   
    print "\nPrint Table \"final\" data with columns names: "
    # cur.execute("SELECT * FROM final where id < 20")
    cur.execute("SELECT * FROM final where axid < 20 order by axid")
    col_names = [cn[0] for cn in cur.description]
    
    rows = cur.fetchall()
    
    # print tabulate(rows, col_names, tablefmt="grid")
    print tabulate(rows, col_names)


def get_max_vaues_from_table_active_final(cur):
#    print "\nGet Max values from Table \"active_final\": "
    cur.execute('PRAGMA table_info(active_final)')
    data = cur.fetchall()
    maxs = ""
    for d in data:
        maxs+= " max(" + d[1] + ")," 
    maxs = maxs[:-1]
    #print "maxs: " + maxs
    cur.execute("SELECT "+ maxs + " FROM active_final")
    results = cur.fetchall()
    #print "results: "
    #print results
    return results;

def create_temptable_dbf_file(col_names, max_col_values):
    col_sizes = []
    for num in max_col_values[0]:
        col_sizes.append(" N("+`len(str(num))`+",0); ")
    #print "col_sizes: " 
    #print col_sizes
    c = [j for i in zip(col_names, col_sizes) for j in i]
    #print "c: " 
    #print c

    myString = "".join(c )
    myString = myString[:-2]

#    print "myString: " + myString
    table = dbf.Table('files/test_output_table', myString)
    table.open() 
    rec = dbf.create_template(table) 

    for datum in rows:
                rec = datum
                table.append(rec) 


con = lite.connect('db/test.db')

with con:    
    
    cur = con.cursor()    

    print_table_info("final")

    print_table_from_query()

    cur.execute("DROP TABLE IF EXISTS active_final")
    cur.execute("CREATE TABLE active_final AS \
        SELECT id, objectid, criteria, axid, count_crit, axid*2 as axidNew \
        FROM final \
        WHERE axid = 18"
        )

    print "\nPrint Table \"active_final\" data with columns names: "
    cur.execute("SELECT * FROM active_final")
    col_names = [cn[0] for cn in cur.description]
    
    rows = cur.fetchall()
    
    # print tabulate(rows, col_names, tablefmt="grid")
    print tabulate(rows, col_names)


    max_col_values = get_max_vaues_from_table_active_final(cur)

    create_temptable_dbf_file(col_names, max_col_values)
    

