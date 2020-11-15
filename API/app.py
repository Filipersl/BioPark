from flask import Flask, jsonify, request, render_template
from message import Message, append_message, get_messages, delete_message

app = Flask(__name__)

#Endpoint para receber uma solicitação de agendamento de mensagem
#POST - /schedule {date:, recipient:, text:, type:}
@app.route('/schedule', methods = ['POST'])
def create_schedule():
    request_data = request.get_json()
    new_Message = Message(request_data['date'], request_data['recipient'], request_data['text'], request_data['type'],request_data['id'])
    append_message(new_Message)
    return jsonify(new_Message.json_map()), 201

#Endpoint para enviar todas as mensagens
#GET - /schedules
@app.route('/schedules', methods = ['GET'])
def get_schedules():
    json_all_messages = {'messages' : []}
    allMessages = get_messages()
    for message in allMessages:
        json_all_messages['messages'].append(message.json_map())
    return jsonify(json_all_messages), 200

#Endpoint para deletar um agendamento de menssagem
#POST - /delete/schedule {date:, recipient:, text:, type:, id:}
@app.route('/delete/schedule', methods = ['POST'])
def delete_schedule():
    finded = False
    request_data = request.get_json()
    new_Message = Message(request_data['date'], request_data['recipient'], request_data['text'], request_data['type'], request_data['id'])
    allMessages = get_messages()
    for message in allMessages:
        if new_Message.compare(message):
            allMessages.remove(message)
            finded = True
    if finded: 
        return jsonify(new_Message.json_map())
    else: 
        return jsonify({'message' : 'Menssagem não encontrada!'})

app.run()