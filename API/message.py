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