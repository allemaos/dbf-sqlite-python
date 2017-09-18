#!/bin/zsh

#activate the virtual environment
source virt_env/virt1/bin/activate

./dbf2sqlite files/test_output_table.dbf -o db/test.db

echo "end of dbftsqlite"

./test-run-results-sqlite3.py

#exit from virtualenv
deactivate

