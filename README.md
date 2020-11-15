# BioPark
- Para rodar os endpoints deve-se ter o python versão 3 ou maior e instalar o flask através do comando:
pip install flask

 - criar uma base de dados do MySQL: 
CREATE DATABASE Schedules;
USE Schedules;

criar a tabela: 
CREATR TABLE message( 
id INT(4) AUTO_INCERMENT,
date VARCHAR(10) NOT NULL,
recipient VARCHAR(30) NOT NULL,
text VARCHAR(500) NOT NULL,
type VARCHAR(10) NOT NULL,
PRIMARY KEY (id)
)

- Depois de ter o banco criado e o flask instalado, navege até a pasta API e digite o comando:
python app.py

- Copie o ip que aparecerá (provavelmente será http://127.0.0.1:5000/)
- Abra algum editor de requisições (Ex: Postman)

Endpoints: 
- Endpoint para receber uma solicitacao de agendamento de mensagem
POST - /schedule {date:, recipient:, text:, type:}
- Endpoint para enviar todas as mensagens
GET - /schedules
- Endpoint para deletar um agendamento de menssagem
POST - /delete/schedule {date:, recipient:, text:, type:, id:}


Sou desenvolvedor Mobile então não possuo experiencia com criação de APIs.
Então, devido a curva de aprendizagem, não realizei toda a proposta, ficou faltando os testes unitários.

Esse foi o meu trabalho, obrigado pela atenção.
Filipe Lopes
