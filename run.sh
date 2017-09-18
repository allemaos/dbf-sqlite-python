#!/bin/zsh

#activate the virtual environment
source virt_env/virt1/bin/activate

./dbf2sqlite files/final.dbf -o db/test.db

./test2-sqlite3.py

#exit from virtualenv
deactivate