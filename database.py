import mysql.connector

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'biblioteca_online'
}

def connect_db():
    conn = mysql.connector.connect(**config)
    return conn
