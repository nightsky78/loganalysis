Simple programm to evaluate the access stats of a news website.

How to run:
Prerequisite: Set up DB as described in the Udacity project outline.
1. execute create_views.sql in the database
2. configure the connection parameter in the DB.config according
   to your enviroment
3. run python3 execute_query,py

Files:
./db.py - main class for all database operations
./DB.config - contains the connection parameters for the database
./execute_query.py - contains code to call DB class and print results
./create_views.sql - create views in the database required for execution of the code
./readme.md - this file
./output.txt - sample output after running this programm
./groupbyip.sql - sql snippet to possibly change the script to
  count multiple accesses from the same IP as one access.
