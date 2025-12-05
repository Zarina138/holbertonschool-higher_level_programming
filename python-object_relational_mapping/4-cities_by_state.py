#!/usr/bin/python3
"""
 a script that lists all cities from the database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    
    db = MySQLdb.connect(
        user=user_name,
        passwd=password,
        db=db_name,
        host="localhost",
        port=3306
    )

curs = db.cursor()
curs.execute("SELECT * FROM cities ORDER BY id ASC")

rows = curs.fetchall()
for row in rows:
    print(row)

curs.close()
db.close()