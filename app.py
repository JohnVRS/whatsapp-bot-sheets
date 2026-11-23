from flask import Flask, request, jsonify
from services.gemini_service import interpretar_mensagem
from services.sheets_service import inserirLinha

my_secret_token = 'meu_token_whatsapp_123'


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, server!</p>"

@app.route("/webhook", methods=['GET','POST'])
def webhook():
    if request.method == 'GET':

        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        desafio = request.args.get('hub.challenge')

        if mode == 'subscribe' and token == my_secret_token:
            print(request.args)
            return desafio
        else:
            return 'Token inválido', 403

    if request.method == 'POST':
        rawMessage = request.get_json()
        message = rawMessage["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]

        #print(" JSON Recebido no POST:", dados)
        #enviar para gemini + gspread

        data_json = interpretar_mensagem(message)
        inserirLinha(data_json)
        print(data_json)

        return "EVENT_RECEIVED", 200