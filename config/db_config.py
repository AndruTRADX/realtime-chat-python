import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="chat_user",
        password="tu_contraseña",
        database="chat_app"
    )
    return db
