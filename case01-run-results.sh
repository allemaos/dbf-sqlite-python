#!/bin/zsh

#activate the virtual environment
source virt_env/virt1/bin/activate

./dbf2sqlite temptable.dbf -o db/sqlite3.db

echo "end of dbftsqlite"

./case01-results.py

#exit from virtualenv
deactivate

