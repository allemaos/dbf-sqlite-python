#!/bin/zsh

./dbf2sqlite files/final.dbf -o db/test.db

./test2-sqlite3.py

