import mysql.connector
import os

DB_PASS = open('/run/secrets/db_password').read().strip()
DB_HOST = os.getenv("DB_HOST", "db")

def create_db_if_not_exists():
    mysqldb = mysql.connector.connect(
        host=DB_HOST, user="root", passwd=DB_PASS
    )
    mysql_cursor = mysqldb.cursor()
    query = "CREATE DATABASE IF NOT EXISTS users_db"
    mysql_cursor.execute(query)
    mysql_cursor.execute("SHOW DATABASES")
