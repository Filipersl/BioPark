from database import open_connection, close_connection, create_schedule, read_schedules, delete_scedule
class Message:
    def __init__(self, date, recipient, text, type, id):
        self.date = date
        self.recipient = recipient
        self.text = text
        self.type = type
        self.id = id
    
    def json_map(self):
        json_message = {
            'id' : self.id,
            "date" : self.date, 
            "recipient" : self.recipient, 
            "text" : self.text,
            "type" : self.type
            }
        return json_message

    def compare(self, message):
        if self.id == message.id:
            return True
        else: 
            return False

def append_message(message):
    con = open_connection('localhost', 'root','', 'Schedules')
    create_schedule(con, message)
    close_connection(close_connection)

def get_messages():
    con = open_connection('localhost', 'root','', 'Schedules')
    allMessages = read_schedules(con)
    close_connection(close_connection)
    return allMessages

def delete_message(message):
    con = open_connection('localhost', 'root','', 'Schedules')
    delete_scedule(con, message)
    close_connection(close_connection)