peaches & mangoes: Anastasia Lee, Nia Lam, Naomi Lai

DISCOVERIES:
----------------------------------------------------
* DictReader: csv file -> python dictionary
  * each row is a dictionary
* csv.DictReader(<file_name>)
* winget install sqlite.sqlite on powershell (windows) or ssh onto stuy computer to run SQLite
* sqlite3 discobandit.db "SELECT * FROM <table_name>;"
* sqlite.connect(<file_name>) opens the file if it exists, creates one otherwise
 * if you don’t delete the .db file between runs, it won’t create a new file because the file already exists

* c = db.cursor() – use cursor to execute commands
* c.execute(<command>) to run SQL statement
* “CREATE TABLE <table_name> (<arg1> <arg1_type>, <arg2> <arg2_type>)”
  * similar to function headers in java
* “INSERT INTO <table_name> (<arg1>, <arg2>, <arg3>) VALUES (<value1>, <value2>, value3>);”

* db.commit() to save changes
* db.close() to close the database
====================================================


QUESTIONS/COMMENTS/CONCERNS:
----------------------------------------------------
Q: does it matter whether we install SQLite in a venv?
Q: do we always have to delete db between runs each time, or is there a way around this?
C: must be careful with the preexistence and creation of new databases
Q: why is there a semicolon at INSERT and sqlite3 disco..db, and not CREATE TABLE? when do we need semicolons?
Q: what is the cursor?
====================================================
