#!/bin/zsh

./dbf2sqlite temptable.dbf -o db/test.db

echo "end of dbftsqlite"

./test3-sqlite3.py



