#!/bin/zsh

#activate the virtual environment
source virt_env/virt1/bin/activate

mkdir -p db

./dbf2sqlite files/final.dbf -o db/sqlite3.db

./case01-main.py

#exit from virtualenv
deactivate