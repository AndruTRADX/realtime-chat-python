# models/db.py
from config.db_config import get_db_connection

def create_room(code):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO rooms (code) VALUES (%s)", (code,))
    connection.commit()
    cursor.close()
    connection.close()

def save_message(room_code, user_name, message):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO messages (room_code, user_name, message) VALUES (%s, %s, %s)", (room_code, user_name, message))
    connection.commit()
    cursor.close()
    connection.close()

def get_messages(room_code):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT user_name, message, sent_at FROM messages WHERE room_code = %s ORDER BY sent_at ASC", (room_code,))
    messages = cursor.fetchall()
    cursor.close()
    connection.close()
    return messages
