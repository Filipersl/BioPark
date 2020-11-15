import mysql.connector
from message import Message

def open_connection(host, user, password, database):
    connection = mysql.connector.connect(host = host, user = user, password = '', database = database)
    if connection.is_connected():
        print('Conectado ao servidor MySQL')
        return connection
    else:
        print('Nao conseguimos conexao')

def close_connection(connection):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        print('Conexao fechada')
    else:
        print('Nao existe conexao')

def read_db_schedules():
    connection = open_connection('localhost', 'root','', 'Schedules')
    cursor = connection.cursor()
    sql = "SELECT id, date, recipient, text, type from message;"
    cursor.execute(sql)
    allMessages = []
    for (id, date, recipient, text, type) in cursor:
        allMessages.append(Message(date, recipient, text, type, id))
    cursor.close()
    close_connection(connection)
    return allMessages

def delete_db_schedule(message): 
    connection = open_connection('localhost', 'root','', 'Schedules')
    cursor = connection.cursor()
    sql = "DELETE FROM message WHERE id = %d"
    values = (message['id'])
    cursor.execute(sql, values)
    cursor.close()
    connection.commit()
    close_connection(connection)

def create_db_schedule(message):
    connection = open_connection('localhost', 'root','', 'Schedules')
    cursor = connection.cursor()
    sql = "INERT INTO message (date, recipient, text, type) values (%s, %s, %s, %s)"
    values = (message['date'], message['recipient'], message['text'], message['type'])
    cursor.execute(sql, values)
    cursor.close()
    connection.commit()
    close_connection(connection)
    
