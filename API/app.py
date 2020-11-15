from flask import Flask, jsonify, request, render_template
from message import Message
from database import read_db_schedules, delete_db_schedule, create_db_schedule

app = Flask(__name__)

#Endpoint para receber uma solicitacao de agendamento de mensagem
#POST - /schedule {date:, recipient:, text:, type:}
@app.route('/schedule', methods = ['POST'])
def create_schedule():
    request_data = request.get_json()
    new_Message = Message(request_data['date'], request_data['recipient'], request_data['text'], request_data['type'],request_data['id'])
    create_db_schedule(new_Message)
    return jsonify(new_Message.json_map()), 201

#Endpoint para enviar todas as mensagens
#GET - /schedules
@app.route('/schedules', methods = ['GET'])
def get_schedules():
    json_all_messages = {'messages' : []}
    allMessages = read_db_schedules()
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
    allMessages = read_db_schedules()
    for message in allMessages:
        if new_Message.compare(message):
            delete_db_schedule(new_Message)
            finded = True
    if finded: 
        return jsonify(new_Message.json_map())
    else: 
        return jsonify({'message' : 'Menssagem nao encontrada!'})

app.run()