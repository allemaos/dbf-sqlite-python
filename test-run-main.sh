#!/bin/zsh

#activate the virtual environment
source virt_env/virt1/bin/activate

mkdir -p db
./dbf2sqlite files/final.dbf -o db/test.db

./test-run-main-sqlite3.py

#exit from virtualenv
deactivate