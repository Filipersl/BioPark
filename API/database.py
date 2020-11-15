import mysql.connector
from message import Message

def open_connection(host, user, password, database):
    connection = mysql.connector.connect(host = host, user = user, password = '', database = database)
    if connection.is_connected():
        print('Conectado ao servidor MySQL')
        return connection
    else:
        print('Não conseguimos conexão')

def close_connection(connection):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        print('Conexão fechada')
    else:
        print('Não existe conexão')

def create_schedule(connection, message):
    cursor = connection.cursor()
    sql = "INERT INTO message (date, recipient, text, type) values (%s, %s, %s, %s)"
    values = (message['date'], message['recipient'], message['text'], message['type'])
    cursor.execute(sql, values)
    cursor.close()
    connection.commit()

def read_schedules(connection):
    cursor = connection.cursor()
    sql = "SELECT id, date, recipient, text, type from message;"
    cursor.execute(sql)
    allMessages = []
    for (id, date, recipient, text, type) in cursor:
        allMessages.append(Message(date, recipient, text, type, id))
    cursor.close()
    return allMessages

def delete_scedule(connection, message): 
    cursor = connection.cursor()
    sql = "DELETE FROM message WHERE id = %d"
    values = (message['id'])
    cursor.execute(sql, values)
    cursor.close()
    connection.commit()