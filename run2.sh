#!/bin/zsh

#activate the virtual environment
source virt_env/virt1/bin/activate

./dbf2sqlite temptable.dbf -o db/test.db

echo "end of dbftsqlite"

./test3-sqlite3.py

#exit from virtualenv
deactivate

