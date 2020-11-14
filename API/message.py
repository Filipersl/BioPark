class Message:
    def __init__(self, date, recipient, text, type):
        self.date = date
        self.recipient = recipient
        self.text = text
        self.type = type
    
    def json_map(self):
        json_message = {
            "date" : self.date, 
            "recipient" : self.recipient, 
            "text" : self.text,
            "type" : self.type
            }
        return json_message

    def compare(self, message):
        if self.date == message.date:
            if self.recipient == message.recipient:
                if self.text == message.text:
                    if self.type == message.type:
                        return True
        return False

#Globais temporarias

allMessages = [Message("10/10/2012", "teste@teste.com", "Bom dia", "E-mail")]

def append_message(message):
    allMessages.append(message)